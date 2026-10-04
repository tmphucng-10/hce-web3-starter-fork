# SPEC - Lab 4: Đánh giá Rủi ro và Phân quyền Hợp đồng Thông minh

## 1. Mục tiêu kiểm định
Phân tích và đối chiếu mức độ rủi ro tiềm ẩn của ba mô hình token (`ClubTokenA`, `ClubTokenB`, `ClubTokenC`) dựa trên cấu trúc phân quyền và mã nguồn mở.

## 2. Phạm vi khảo sát mã nguồn (`ClubTokens.sol`)
- **ClubTokenA (Dòng 7-11):** Token chuẩn thuần túy, không tích hợp cơ chế quản trị nâng cao.
- **ClubTokenB (Dòng 13-21):** Tích hợp mô hình sở hữu (`Ownable`) kèm chức năng mở rộng nguồn cung.
- **ClubTokenC (Dòng 23-38):** Tích hợp mô hình kiểm soát dòng tiền và trạng thái tài khoản.

## 3. Tổng hợp đánh giá rủi ro chuyên sâu

| Mã định danh | Cơ chế quản trị | Hàm trọng yếu | Mức độ rủi ro | Phân tích tác động đối với nhà đầu tư |
| :--- | :--- | :--- | :--- | :--- |
| **ClubTokenA** | Phi tập trung hoàn toàn (Không có chủ sở hữu) | Không có | **Thấp (An toàn)** | Tổng cung cố định ngay từ khối khởi tạo (`constructor`), không ai có quyền can thiệp hay in thêm, đảm bảo tính minh bạch tối đa. |
| **ClubTokenB** | Tập trung (Có quản trị viên `Ownable`) | `mint(address, uint256)` (Dòng 18-20) | **Trung bình - Cao** | Chủ sở hữu có toàn quyền phát hành vô hạn lượng token mới, gây nguy cơ pha loãng giá trị tài sản của cộng đồng nắm giữ. |
| **ClubTokenC** | Kiểm soát toàn diện (Quản trị + Danh sách đen) | `setRestricted` (Dòng 30-32) | **Cao (Rủi ro đóng băng)** | Quản trị viên có khả năng chặn quyền chuyển giao tài sản của các địa chỉ cụ thể, tạo rủi ro mất thanh khoản cho người dùng. |

## 4. Kết luận kỹ thuật
Các hợp đồng tích hợp quyền hạn mở rộng (như ClubTokenB và ClubTokenC) đòi hỏi người dùng phải cực kỳ thận trọng và đặt niềm tin lớn vào độ uy tín của bên phát hành, vì các "cửa hậu" (backdoor) quản trị có thể tác động trực tiếp đến quyền lợi nhà đầu tư.