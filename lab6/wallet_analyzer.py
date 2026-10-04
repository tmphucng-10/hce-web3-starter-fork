import os
import sys
import time
import datetime
import requests
import matplotlib.pyplot as plt

def get_transactions(api_key, address, days):
    cutoff_time = int(time.time()) - (days * 24 * 3600)
    page = 1
    offset = 10000
    transactions = []
    
    while True:
        url = "https://api.etherscan.io/v2/api"
        params = {
            "chainid": 1,
            "module": "account",
            "action": "txlist",
            "address": address,
            "startblock": 0,
            "endblock": 99999999,
            "page": page,
            "offset": offset,
            "sort": "desc",
            "apikey": api_key
        }
        
        try:
            response = requests.get(url, params=params)
            if response.status_code != 200:
                print(f"Lỗi kết nối API: HTTP {response.status_code}")
                sys.exit(1)
                
            data = response.json()
        except Exception as e:
            print(f"Lỗi khi gọi API: {e}")
            sys.exit(1)
            
        if data.get("status") == "0" and data.get("message") != "No transactions found":
            print(f"Lỗi từ Etherscan API: {data.get('result')}")
            sys.exit(1)
            
        txs = data.get("result", [])
        if not txs or not isinstance(txs, list):
            break
            
        reached_cutoff = False
        for tx in txs:
            tx_time = int(tx["timeStamp"])
            if tx_time >= cutoff_time:
                transactions.append(tx)
            else:
                reached_cutoff = True
                break
                
        if reached_cutoff or len(txs) < offset:
            break
            
        page += 1
        
    # Đảo ngược danh sách để các giao dịch xếp theo thời gian tăng dần (cũ nhất -> mới nhất)
    transactions.reverse()
    return transactions

def main():
    api_key = os.environ.get("ETHERSCAN_API_KEY")
    if not api_key:
        print("Lỗi: Không tìm thấy biến môi trường ETHERSCAN_API_KEY.")
        sys.exit(1)
        
    while True:
        address = input("Nhập địa chỉ ví Ethereum: ").strip()
        if len(address) == 42 and address.startswith("0x"):
            break
        print("Lỗi: Địa chỉ ví không hợp lệ (phải gồm 42 ký tự và bắt đầu bằng 0x).")
        
    days_input = input("Nhập số ngày phân tích (mặc định 90): ").strip()
    days = 90
    if days_input:
        try:
            days = int(days_input)
        except ValueError:
            print("Số ngày không hợp lệ, sử dụng mặc định 90 ngày.")
            
    print(f"Đang lấy dữ liệu {days} ngày gần nhất...")
    txs = get_transactions(api_key, address, days)
    
    if not txs:
        print("Vi khong co giao dich trong ky")
        sys.exit(0)
        
    cumulative_balance = 0.0
    total_in = 0.0
    total_out = 0.0
    
    table_data = []
    times = []
    balances = []
    
    addr_lower = address.lower()
    
    for tx in txs:
        dt = datetime.datetime.fromtimestamp(int(tx["timeStamp"]))
        tx_time_str = dt.strftime('%Y-%m-%d %H:%M:%S')

        is_error = tx.get("isError") == "1"
        value_eth = int(tx.get("value", 0)) / 10**18
        fee_eth = (
            int(tx.get("gasUsed", 0))
            * int(tx.get("gasPrice", 0))
        ) / 10**18

        is_out = (tx.get("from", "").lower() == addr_lower)
        is_in = (tx.get("to", "").lower() == addr_lower)

        # Xử lý giao dịch Ra
        if is_out:
            if is_error:
                cumulative_balance -= fee_eth
                total_out += fee_eth

                table_data.append([
                    tx_time_str,
                    "Ra",
                    0.0,
                    fee_eth,
                    cumulative_balance
                ])

            else:
                cumulative_balance -= (value_eth + fee_eth)
                total_out += (value_eth + fee_eth)

                table_data.append([
                    tx_time_str,
                    "Ra",
                    value_eth,
                    fee_eth,
                    cumulative_balance
                ])

            times.append(dt)
            balances.append(cumulative_balance)

        # Xử lý giao dịch Vào
        if is_in:
            if not is_error:
                cumulative_balance += value_eth
                total_in += value_eth

            table_data.append([
                tx_time_str,
                "Vào",
                value_eth,
                fee_eth,
                cumulative_balance
            ])

            times.append(dt)
            balances.append(cumulative_balance)

    # In bảng kết quả
    print(f"\n{'Thời gian':<20} | {'Loại':<5} | {'Số tiền (ETH)':<15} | {'Phí (ETH)':<15} | {'Số dư lũy kế (ETH)':<18}")
    print("-" * 85)
    for row in table_data:
        print(f"{row[0]:<20} | {row[1]:<5} | {row[2]:<15.6f} | {row[3]:<15.6f} | {row[4]:<18.6f}")
    print("-" * 85)
    
    # In thông số tổng hợp
    print("\nCÁC CHỈ TIÊU TỔNG HỢP:")
    print(f"- Tổng dòng tiền vào: {total_in:.6f} ETH")
    print(f"- Tổng dòng tiền ra: {total_out:.6f} ETH")
    print(f"- Số dư cuối kỳ: {cumulative_balance:.6f} ETH")
    
    # Vẽ và lưu biểu đồ
    try:
        os.makedirs("lab6", exist_ok=True)
        output_path = os.path.join("lab6", "Bieu_do_duong.png")
        
        plt.figure(figsize=(10, 6))
        plt.plot(times, balances, marker='.', linestyle='-', color='b')
        plt.title(f"Số dư lũy kế dòng tiền của ví trong {days} ngày qua")
        plt.xlabel("Thời gian")
        plt.ylabel("Số dư lũy kế (ETH)")
        plt.grid(True)
        plt.tight_layout()
        
        plt.savefig(output_path)
        print(f"\nĐã tự động lưu tệp biểu đồ tại: {output_path}")
        plt.show()
    except Exception as e:
        print(f"\nKhông thể hiển thị biểu đồ: {e}")

if __name__ == "__main__":
    main()