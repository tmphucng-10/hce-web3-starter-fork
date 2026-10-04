# SPEC - Lab 5: Xây dựng Đặc tả Kỹ thuật Công cụ Phân tích Dòng tiền On-Chain

## 1. Mục tiêu
Thiết lập tài liệu đặc tả chi tiết cho ứng dụng theo dõi dòng tiền ra/vào của một địa chỉ ví trong khung thời gian mặc định 90 ngày, đồng thời thống kê số dư tích lũy theo chiều thời gian. 

Mục tiêu cốt lõi là định nghĩa rõ ràng các yêu cầu kỹ thuật để lập trình viên hoặc công cụ AI có thể triển khai hệ thống chính xác ngay từ lần đầu tiên.

## 2. Dữ liệu Đầu vào (Inputs)
- **Địa chỉ ví mục tiêu:** Chuỗi định danh Ethereum hợp lệ (định dạng chuẩn 0x kèm theo tổng cộng 42 ký tự).
- **Khóa xác thực API:** Lấy trực tiếp từ biến môi trường hệ thống (`ETHERSCAN_API_KEY`).
- **Khoảng thời gian khảo sát:** Mặc định thiết lập mốc 90 ngày gần nhất tính từ thời điểm thực thi.

## 3. Quy tắc Vận hành Nghiệp vụ (Business Rules)
- **R1:** Xác định dòng tiền vào dựa trên điều kiện trường `to` trùng khớp với địa chỉ ví phân tích.
- **R2:** Xác định dòng tiền ra dựa trên điều kiện trường `from` trùng khớp với địa chỉ ví phân tích.
- **R3:** Tổng giá trị tài sản bị trừ thực tế đối với một giao dịch chuyển đi thành công được tính bằng tổng số tiền chuyển cộng với khoản phí mạng (`Gas Fee`).
- **R4:** Các giao dịch ở trạng thái thất bại (`Failed`) vẫn phát sinh chi phí mạng, khoản phí này bắt buộc phải được hạch toán vào tổng dòng tiền ra.
- **R5:** Toàn bộ dữ liệu định mức thô lấy từ API (tính theo đơn vị wei) phải được quy đổi chuẩn xác sang đơn vị ETH bằng cách chia cho `10^18` trước khi xuất kết quả.
- **R6:** Sắp xếp danh sách giao dịch theo chiều thời gian tăng dần (từ các bản ghi cũ nhất đến các giao dịch phát sinh gần nhất).
- **R7:** Phạm vi xử lý chỉ tập trung vào các giao dịch đồng coin gốc (ETH native transactions) của tài khoản.
- **R8:** Lọc và chỉ giữ lại các giao dịch nằm trọn vẹn trong khung thời gian yêu cầu.

## 4. Dữ liệu Đầu ra (Outputs)

### 4.1. Sổ cái giao dịch chi tiết
Bảng dữ liệu tối thiểu bao gồm các trường thông tin:
- Mốc thời gian thực hiện giao dịch.
- Phân loại chiều giao dịch (`Vào` hoặc `Ra`).
- Khối lượng giao dịch tính bằng ETH.
- Chi phí giao dịch phát sinh.
- Biến động số dư lũy kế sau từng giao dịch.

### 4.2. Trực quan hóa dữ liệu
- Biểu đồ tuyến tính biểu diễn sự biến động của số dư tích lũy theo dòng thời gian (Trục hoành: Thời điểm; Trục tung: Số dư tương ứng).

### 4.3. Các chỉ số tổng quan cốt lõi
- Tổng giá trị dòng tiền vào trong kỳ.
- Tổng giá trị dòng tiền ra trong kỳ.
- Số dư tài sản ròng tại thời điểm cuối kỳ.

## 5. Xử lý Tình huống Ngoại lệ (Exceptions)
- **Danh sách trống:** Nếu API trả về dữ liệu rỗng, hệ thống ghi nhận thông báo `Vi khong co giao dich trong ky` và tiến hành kết thúc mượt mà không văng lỗi.
- **Mã lỗi hệ thống:** Trường hợp API phản hồi mã lỗi, tiến trình phải dừng lập tức và xuất thông báo lỗi chi tiết.
- **Dữ liệu lớn (>10.000 bản ghi):** Tự động kích hoạt cơ chế phân trang để gom đủ toàn bộ dữ liệu lịch sử.
- **Sai định dạng ví:** Từ chối xử lý và yêu cầu cung cấp lại địa chỉ hợp lệ nếu chuỗi ký tự đầu vào không đạt chuẩn.
- **Thiếu khóa cấu hình:** Dừng thực thi ngay lập tức và cảnh báo thiếu biến môi trường `ETHERSCAN_API_KEY` nếu chưa được thiết lập.

## 6. Giới hạn Phạm vi (Out of Scope)
- Không can thiệp hoặc xử lý các loại token tiêu chuẩn ERC-20 (như USDT, USDC...).
- Không quy đổi giá trị tài sản sang tiền pháp định (VND, USD...).
- Không tích hợp cơ chế tra cứu biểu đồ giá thị trường của ETH.
- Không tương tác ghi dữ liệu hoặc phát sinh giao dịch trên mạng lưới blockchain.
- Không lưu trữ hoặc yêu cầu người dùng cung cấp thông tin nhạy cảm như Private Key hay Seed Phrase.