# LAB 7 — TÍNH CHI PHÍ VẬN HÀNH THỰC TẾ

## 1. Công thức tính chi phí

Giải thích ngắn gọn:
- 1 Gwei = $10^{-9}$ ETH
- Chi phí một giao dịch bằng ETH: $\text{Gas Used} \times \text{Gas Price (Gwei)} \times 10^{-9}$
- Chi phí một giao dịch bằng USD: $\text{Chi phí (ETH)} \times \text{Giá ETH (USD/ETH)}$
- Chi phí vận hành một tháng: $\text{Chi phí 1 giao dịch (USD)} \times \text{Số lượng giao dịch/tháng}$

## 2. Bài toán câu lạc bộ tích điểm

### 2.1. Dữ liệu đầu vào

- Số giao dịch/tháng = 1.000
- Gas Price = 20 Gwei
- Giá ETH = 3.000 USD/ETH
- Layer 2 rẻ hơn khoảng 100 lần
- Gas Used = chưa xác định

### 2.2. Chi phí trên Ethereum Mainnet

Gọi $G$ là Gas Used của một giao dịch cộng điểm.

Tính từng bước theo $G$:

1. **Chi phí một giao dịch bằng ETH:**
   $$\text{Chi phí (ETH)} = G \times 20 \times 10^{-9}$$

2. **Chi phí một giao dịch bằng USD:**
   $$\text{Chi phí (USD)} = (G \times 20 \times 10^{-9}) \times 3.000 = G \times 60 \times 10^{-6}$$

3. **Chi phí 1.000 giao dịch/tháng bằng ETH:**
   $$\text{Tổng ETH/tháng} = (G \times 20 \times 10^{-9}) \times 1.000 = G \times 20 \times 10^{-6}$$

4. **Chi phí 1.000 giao dịch/tháng bằng USD:**
   $$\text{Tổng USD/tháng} = (G \times 60 \times 10^{-6}) \times 1.000 = G \times 0,06$$

### 2.3. Chi phí trên Layer 2

Dựa trên giả định đề bài, Layer 2 rẻ hơn khoảng 100 lần so với Mainnet.

| Nền tảng | Công thức chi phí 1.000 giao dịch/tháng (USD) |
| :--- | :--- |
| **Ethereum Mainnet** | $G \times 0,06$ |
| **Layer 2** | $\frac{G \times 0,06}{100} = G \times 0,0006$ |

## 3. Phân tích tính khả thi

### 3.1. Ai chịu phí?
- **Nếu câu lạc bộ trả phí:** Mô hình dễ tiếp cận cho sinh viên, nhưng câu lạc bộ cần có nguồn tài chính hoặc quỹ hỗ trợ bền vững để duy trì hoạt động hàng tháng.
- **Nếu sinh viên trả phí:** Giảm gánh nặng tài chính cho ban tổ chức, nhưng có thể làm giảm động lực tham gia của sinh viên.

### 3.2. Sinh viên có chấp nhận chi phí không?
Xét về góc độ kinh tế, nếu phí giao dịch on-chain lớn hoặc xấp xỉ so với giá trị thực tế của điểm thưởng hoặc quyền lợi nhận được, việc yêu cầu sinh viên tự chi trả phí sẽ khiến mô hình khó được chấp nhận rộng rãi.

### 3.3. Kết luận
Chưa thể đưa ra một con số chi phí cuối cùng vì chưa có dữ liệu Gas Used thực tế:
- Chi phí trên Mainnet phụ thuộc tuyến tính vào biến $G$ ($\text{Gas Used}$).
- Chi phí trên Layer 2 được ước tính giảm khoảng 100 lần theo giả định của đề bài.
- Kết luận chính thức về mức chi phí sẽ được cập nhật khi đo đạc được Gas Used thực tế.

## 4. Mở rộng cho ý tưởng đồ án nhóm

### Ý tưởng: Quỹ nhóm nhiều người duyệt
- **Người dùng:** Nhóm sinh viên có quỹ chung cần quản lý tài chính minh bạch.
- **Vấn đề cần giải quyết:** Tránh tình trạng lạm dụng quỹ cá nhân và đảm bảo mọi khoản chi tiêu đều có sự đồng thuận công khai từ các thành viên.
- **Thao tác blockchain chính:**
  1. Tạo đề nghị chi.
  2. Phê duyệt đề nghị.
  3. Thực hiện khoản chi.

### Phân tích số lượng giao dịch (Trường hợp giả định 3 người duyệt, cần 2/3 đồng ý):
Một đề nghị chi hoàn chỉnh bao gồm:
- 1 giao dịch tạo đề nghị.
- 2 giao dịch phê duyệt (đạt đủ tỷ lệ 2/3).
- 1 giao dịch thực hiện khoản chi (đảm bảo chỉ thực hiện một lần sau khi đủ phê duyệt).
Tổng cộng có **4 giao dịch** cho một đề nghị chi hoàn chỉnh.

Gọi $N$ là số đề nghị chi trong một tháng, ta có:
$$\text{Số giao dịch/tháng} = 4 \times N$$

### Công thức tổng quát chi phí:
Gọi lần lượt Gas Used của từng thao tác là $G_{\text{tao}}$, $G_{\text{duyet}}$, và $G_{\text{thuchien}}$.
Tổng Gas Used cho một đề nghị hoàn chỉnh là:
$$\text{Tổng Gas/đề nghị} = G_{\text{tao}} + 2 \times G_{\text{duyet}} + G_{\text{thuchien}}$$

### Nhận xét tính khả thi:
Vì mỗi đề nghị chi yêu cầu nhiều bước tương ứng với nhiều giao dịch on-chain khác nhau, tổng chi phí vận hành sẽ tăng tuyến tính theo số lượng đề nghị trong tháng ($N$). Cần tiến hành đo đạc Gas Used thực tế trên Remix cho từng thao tác cụ thể trước khi đưa ra kết luận chi phí tài chính chính xác cuối cùng.