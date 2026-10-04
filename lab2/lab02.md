# Báo cáo Lab 2: Ví và giao dịch đầu tiên

## 1. Bảng tóm tắt giao dịch

| Tiêu chí | Giao dịch thành công | Giao dịch thất bại (cố ý) |
| :--- | :--- | :--- |
| **Mã băm (Tx Hash)** | `0x4883a0703ba1adfa5472dbb536cef10188ac4666c4d4a0be789d8c75e067b973` | Không có mã băm do bị ví chặn lại. |
| **Số tiền (Value)** | 0.05 SepoliaETH | N/A |
| **Phí thực trả** | 0.000052520771037 SepoliaETH | Không mất phí |
| **Trạng thái** | Thành công (Success) | Bị từ chối |
| **Nguyên nhân lỗi** | (Không có) | Sai định dạng địa chỉ nhận (thiếu/sai ký tự) nên ví MetaMask cảnh báo "Địa chỉ không hợp lệ" và vô hiệu hóa nút Gửi. |

## 2. Trả lời câu hỏi
**Câu hỏi:** Nếu bạn chuyển nhầm tiền mã hóa cho một người lạ, bạn có lấy lại được không? Vì sao?

**Trả lời:** 
Không thể lấy lại được (trừ khi người lạ đó tự nguyện chuyển trả lại).
**Vì sao:** Blockchain hoạt động dựa trên cơ chế phi tập trung và tính không thể đảo ngược (immutable). Một khi giao dịch đã được xác thực và ghi vào các khối (block) trên mạng lưới, không có bất kỳ tổ chức trung gian, ngân hàng hay bộ phận hỗ trợ khách hàng nào có quyền can thiệp, hủy bỏ hay đảo ngược giao dịch đó.