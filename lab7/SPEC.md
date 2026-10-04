# SPEC — Lab 7: Tính chi phí vận hành thực tế

## 1. Mục đích

Tính chi phí vận hành hàng tháng của một ứng dụng blockchain dựa trên
số lượng giao dịch, lượng gas tiêu thụ, đơn giá gas và giá ETH;
sau đó so sánh chi phí giữa Ethereum Mainnet và Layer 2 để hỗ trợ
đánh giá tính khả thi của mô hình.

## 2. Đầu vào

- Số lượng giao dịch phát sinh trong một tháng.
- Lượng gas tiêu thụ của một giao dịch (Gas Used).
- Đơn giá gas, đơn vị Gwei.
- Giá ETH, đơn vị USD/ETH.
- Hệ số giảm chi phí khi chuyển sang Layer 2.
- Bài toán mẫu của Lab 7:
  - 1.000 giao dịch cộng điểm mỗi tháng.
  - Gas Price = 20 Gwei.
  - Giá ETH = 3.000 USD.
  - Layer 2 có đơn giá gas rẻ hơn khoảng 100 lần.
- Thông tin về số lượng giao dịch dự kiến của ý tưởng đồ án nhóm.

## 3. Quy tắc nghiệp vụ

- R1: Một lượt cộng điểm được tính là một giao dịch ghi dữ liệu trên blockchain.

- R2: 1 Gwei = $10^{-9}$ ETH.

- R3: Chi phí một giao dịch tính bằng ETH:

  Chi phí giao dịch (ETH)
  = Gas Used × Gas Price (Gwei) × $10^{-9}$.

- R4: Chi phí một giao dịch tính bằng USD:

  Chi phí giao dịch (USD)
  = Chi phí giao dịch (ETH) × Giá ETH (USD).

- R5: Chi phí vận hành một tháng:

  Chi phí tháng
  = Chi phí một giao dịch × Số giao dịch trong tháng.

- R6: Khi tính phương án Layer 2, sử dụng hệ số giảm chi phí được cung cấp.
  Với bài toán mẫu của Lab 7, chi phí Layer 2 được giả định rẻ hơn
  khoảng 100 lần so với phương án Mainnet.

- R7: Khi so sánh các phương án phải sử dụng cùng số lượng giao dịch
  và cùng phạm vi hoạt động để kết quả có thể so sánh.

- R8: Gas Used phải được ghi rõ là số tham khảo, số giả định hoặc
  số đo thực tế; không được trình bày số tham khảo như số đo thực tế.

- R9: Sau khi tính chi phí phải xác định đối tượng chịu phí giao dịch:
  câu lạc bộ, sinh viên hoặc một cơ chế khác của mô hình.

- R10: Kết luận tính khả thi phải dựa trên kết quả chi phí đã tính
  và cách phân bổ chi phí, không chỉ dựa vào việc hệ thống có chạy được hay không.

## 4. Đầu ra

- Một bảng tính chi phí của bài toán câu lạc bộ, gồm tối thiểu:
  - Số giao dịch/tháng.
  - Gas Used/giao dịch.
  - Gas Price.
  - Chi phí một giao dịch bằng ETH.
  - Chi phí một giao dịch bằng USD.
  - Tổng chi phí một tháng bằng ETH.
  - Tổng chi phí một tháng bằng USD.

- Một bảng so sánh:
  - Ethereum Mainnet.
  - Layer 2.

- Câu trả lời cho các vấn đề:
  - Chi phí vận hành một tháng.
  - Chi phí nếu chuyển sang Layer 2.
  - Đối tượng chịu phí.
  - Nhận xét về khả năng người dùng chấp nhận chi phí.

- Một đoạn kết luận về tính khả thi của bài toán mẫu.

- Một phần áp dụng cùng khung tính chi phí cho ý tưởng đồ án nhóm.

- Kết quả được trình bày trong tệp `lab07.md`.

## 5. Trường hợp ngoại lệ

- Nếu chưa có Gas Used thực tế thì phải ghi rõ đây là giá trị
  tham khảo hoặc giả định, không được coi là số đo thực tế.

- Nếu số giao dịch trong tháng bằng 0 thì chi phí vận hành
  theo giao dịch trong tháng bằng 0.

- Nếu Gas Price hoặc giá ETH bằng 0 hoặc không được cung cấp
  thì chưa đủ dữ liệu để tính chi phí USD và phải ghi rõ
  dữ liệu còn thiếu.

- Nếu số giao dịch, Gas Used, Gas Price hoặc giá ETH là số âm
  thì dữ liệu không hợp lệ và không sử dụng để tính toán.

- Nếu hệ số giảm chi phí Layer 2 không được cung cấp thì
  không tự suy đoán tỷ lệ giảm mà phải ghi rõ chưa đủ dữ liệu
  để so sánh.

## 6. Ngoài phạm vi

- Không dự đoán giá ETH trong tương lai.
- Không tính lợi nhuận hoặc doanh thu toàn bộ mô hình kinh doanh.
- Không tính chi phí phát triển phần mềm, máy chủ, nhân sự hoặc marketing.
- Không coi bảng gas tham khảo trong tài liệu là số gas thực tế
  của hợp đồng.
- Không triển khai smart contract trong Lab 7.
- Không thực hiện giao dịch blockchain thật chỉ để tính chi phí.