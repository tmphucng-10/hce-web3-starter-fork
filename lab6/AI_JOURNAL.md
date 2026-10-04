# NHẬT KÝ LÀM VIỆC VỚI AI - Lab 6: Hiện thực hóa Công cụ Phân tích Dòng tiền On-Chain
(Địa chỉ ví kiểm tra: 0xF977814e90dA44bFA03b6295A0616a897441aceC)

## Lần 1

**Prompt:** Đọc tệp `lab05/SPEC.md` và `AGENTS.md`.

Trước khi viết mã, hãy tóm tắt lại cách bạn hiểu yêu cầu của bài toán, gồm:
- đầu vào,
- cách xác định dòng tiền vào/ra,
- cách xử lý phí,
- giao dịch thất bại,
- đổi wei sang ETH,
- phân trang,
- đầu ra,
- ngoại lệ,
- ngoài phạm vi.

Chưa viết code.
Chỉ tóm tắt cách hiểu và chờ tôi xác nhận.

**AI trả về:** AI đã tóm tắt đúng hầu hết yêu cầu trong SPEC:
- Nhận địa chỉ ví, API key từ biến môi trường và số ngày phân tích.
- Xác định giao dịch vào/ra.
- Tính phí giao dịch.
- Xử lý giao dịch thất bại.
- Đổi wei sang ETH.
- Xử lý phân trang.
- Tạo bảng, biểu đồ và các chỉ tiêu tổng hợp.
- Xử lý các trường hợp ngoại lệ và giới hạn phạm vi.

**Đánh giá:** Dùng được

**Chỗ sai:** Không phát hiện lỗi. Tuy nhiên SPEC còn một điểm mơ hồ về cách khởi tạo số dư lũy kế.

**Cách sửa:** Tôi bổ sung quy ước:
- Số dư lũy kế trong bài này là dòng tiền ròng lũy kế trong kỳ.
- Bắt đầu từ 0.
- Tiền vào thành công: cộng giá trị ETH.
- Tiền ra thành công: trừ giá trị chuyển + phí.
- Tiền ra thất bại: chỉ trừ phí.
- Không coi đây là số dư blockchain thực tế của ví.

Sau đó yêu cầu AI xác nhận lại cách hiểu trước khi viết code.

**AI phát hiện:** Sinh viên phát hiện điểm mơ hồ trong SPEC và yêu cầu làm rõ trước khi AI sinh mã.

**Ai xác nhận lại:** AI xác nhận đã hiểu rằng số dư lũy kế là dòng tiền ròng phát sinh trong kỳ, bắt đầu từ 0; giao dịch vào được cộng giá trị, giao dịch ra thành công trừ giá trị và phí, giao dịch ra thất bại chỉ trừ phí.

AI đồng thời xác nhận đây không phải số dư blockchain thực tế của ví.

## Lần 2

**Prompt:** Tôi xác nhận cách hiểu của bạn là đúng.

Bây giờ hãy bắt đầu viết chương trình Python thực hiện đúng toàn bộ yêu cầu trong:
- lab05/SPEC.md
- AGENTS.md
và điểm bổ sung đã thống nhất về "số dư lũy kế dòng tiền trong kỳ".

YÊU CẦU:
1. Tạo chương trình: `lab06/wallet_analyzer.py`
2. Chương trình phải:
   - Nhận địa chỉ ví Ethereum.
   - Đọc khóa API từ biến môi trường ETHERSCAN_API_KEY.
   - Cho phép nhập số ngày phân tích, mặc định 90 ngày.
   - Lấy giao dịch ETH gốc từ Etherscan.
   - Không phân tích token ERC-20.
   - Xác định giao dịch vào/ra đúng theo SPEC.
   - Với giao dịch ra thành công: trừ giá trị chuyển + phí.
   - Với giao dịch ra thất bại: chỉ trừ phí.
   - Đổi wei sang ETH trước khi hiển thị.
   - Xử lý phân trang để không bỏ sót dữ liệu.
   - Sắp xếp giao dịch theo thời gian tăng dần.
   - Tính dòng tiền ròng lũy kế bắt đầu từ 0.
   - Hiển thị bảng giao dịch.
   - Hiển thị tổng dòng tiền vào, tổng dòng tiền ra, số dư lũy kế cuối kỳ.
   - Vẽ biểu đồ đường số dư lũy kế theo thời gian.
   - Xử lý các trường hợp ngoại lệ trong SPEC.
3. Không hardcode API key trong mã nguồn.
4. Không yêu cầu private key hoặc seed phrase.
5. Không sửa các thư mục lab khác hoặc SPEC gốc.
6. Không git commit, không git push.

**AI trả về:** AI tạo chương trình Python `wallet_analyzer.py` để lấy giao dịch từ Etherscan, phân loại dòng tiền vào/ra, tính phí, đổi wei sang ETH, tính số dư lũy kế và vẽ biểu đồ.

**Đánh giá:** Phải sửa

**Chỗ sai:** Chương trình sử dụng endpoint Etherscan V1 cũ (`https://api.etherscan.io/api`), khi chạy thực tế trả về thông báo lỗi `You are using a deprecated V1 endpoint, switch to Etherscan API V2` nên không lấy được dữ liệu.

**Cách sửa:** Tôi yêu cầu AI sửa lại phiên bản API, chuyển sang endpoint V2 (`https://api.etherscan.io/v2/api`) và bổ sung tham số `chainid = 1`.

**AI phát hiện:** Sinh viên phát hiện lỗi phiên bản API và yêu cầu AI sửa lại.

## Lần 3

**Prompt:** Sau khi sửa Etherscan API V1 sang V2, tôi chạy lại chương trình và nhận được lỗi `Missing chainid parameter (required for v2 api)`. Hãy kiểm tra nguyên nhân trong `lab06/wallet_analyzer.py`.

**AI trả về:** AI xác định cần bổ sung tham số `chainid`.

**Đánh giá:** Phải sửa

**Chỗ sai:** Mặc dù khai báo `chainid = 1` trong biến `params`, lệnh gọi chỉ thực thi `requests.get(url)` nên toàn bộ tham số không được gửi đi. 

**Cách sửa:** Yêu cầu sửa thành `requests.get(url, params=params)`. Chương trình sau đó đã chạy thành công.

**Ai phát hiện:** Sinh viên phát hiện.

## Kiểm tra 6 điểm:

### 1. Kiểm tra đơn vị tiền:
- Đối chiếu giao dịch với Etherscan cho thấy kết quả quy đổi từ wei sang ETH hoàn toàn chuẩn xác.
- Bằng chứng: `lab06/Kiem tra don vi ETH.png`

### 2. Kiểm tra khóa API:
- Đọc qua `os.environ.get()`, không hardcode trong mã nguồn. Đạt yêu cầu bảo mật.

### 3. Kiểm tra phân trang:
- Kiểm thử với `offset = 100` và trả về `10000` theo SPEC. Cơ chế phân trang hoạt động tốt.

### 4. Kiểm tra giao dịch thất bại:
- Thống kê giao dịch đi ra có `isError = 1` trên ví kiểm tra cho kết quả bằng 0 trong kỳ.

### 5. Kiểm tra xử lý lỗi:
- Thử nghiệm với API key không hợp lệ trả về thông báo `Lỗi từ Etherscan API: Invalid API Key (#err2)` và dừng mượt mà không văng Traceback.