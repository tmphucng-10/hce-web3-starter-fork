# NHẬT KÝ LÀM VIỆC VỚI AI - Lab 4: Nhận diện hợp đồng có rủi ro

## Lần 1

**Prompt:** Tạo thư mục lab04 trong thư mục gốc dự án.
Sao chép hai file mẫu SPEC.md; AI_JOURNAL.md và lab04.md vào lab04.
Giữ nguyên hai file gốc ở thư mục gốc, không sửa nội dung file gốc.
Không thực hiện thay đổi nào khác.


**AI trả về:** Đã tạo thư mục lab04 và sao chép hai file theo yêu cầu.

**Đánh giá:** Dùng được.

**Chỗ sai:** Không phát hiện.

**Cách sửa:** Không cần sửa.

**Ai phát hiện:** Sinh viên kiểm tra lại cấu trúc thư mục.

## Lần 2

**Prompt:**  Bạn là chuyên viên thẩm định rủi ro tài sản số.

Dưới đây là mã nguồn một hợp đồng token.
Hãy liệt kê mọi quyền đặc biệt mà chủ sở hữu hợp đồng có thể thực hiện.

Với mỗi quyền, nêu:
- Tên hàm
- Số dòng
- Rủi ro cụ thể cho người nắm giữ token

Trình bày dưới dạng bảng.

Chỉ dựa trên mã nguồn tôi cung cấp.
Nếu không tìm thấy quyền nào, hãy nói rõ là không tìm thấy.


Hãy phân tích file:
contracts/lab04/ClubTokens.sol

Ghi nhận vào file lab04.md trong thư mục lab04

**AI trả về:** AI phân tích ba hợp đồng như sau:

- `ClubTokenA`: Không tìm thấy quyền đặc biệt của chủ sở hữu có thể gây rủi ro cho người nắm giữ token.
- `ClubTokenB`: Phát hiện hàm `mint()` tại dòng 18–20 cho phép chủ sở hữu tạo thêm token cho một địa chỉ. Do mã nguồn không đặt giới hạn lượng token được mint, quyền này có thể làm tăng tổng cung và gây pha loãng đối với người đang nắm giữ token.
- `ClubTokenC`: Phát hiện hàm `setRestricted()` tại dòng 30–32 cho phép chủ sở hữu đưa một địa chỉ vào trạng thái bị hạn chế. Cơ chế `_update()` tại dòng 34–36 kiểm tra trạng thái này và ngăn địa chỉ bị hạn chế chuyển token đi.

**Đánh giá:** Phải sửa

**Chỗ sai:** 

1. Với `ClubTokenC`, AI mô tả rằng chủ sở hữu có thể "ngăn chặn giao dịch". Cách diễn đạt này hơi rộng.

   Trong mã nguồn, dòng 35 kiểm tra:

   `require(!restricted[from], "Dia chi bi han che");`

   Vì vậy, chính xác hơn là địa chỉ bị đánh dấu `restricted = true` không thể chuyển token đi. Mã nguồn này không cho thấy địa chỉ đó bị ngăn nhận token.

2. Ban đầu khi đọc thủ công `ClubTokenB`, tôi ghi "Có hàm onlyOwner: Không". Sau khi đối chiếu lại mã nguồn, tôi nhận thấy dòng 18 có từ khóa `onlyOwner`, nên nhận xét ban đầu của tôi là sai.

3. Ban đầu tôi ghi cả `setRestricted()` và `_update()` là tên hàm thể hiện quyền đặc biệt của `ClubTokenC`. Sau khi đối chiếu lại, tôi nhận thấy:
   - `setRestricted()` là hàm mà owner trực tiếp được quyền gọi.
   - `_update()` không phải quyền riêng của owner mà là hàm nội bộ thực hiện việc kiểm tra trạng thái `restricted`.

**Cách sửa:**

- Sửa kết quả đọc thủ công của `ClubTokenB` thành:
  `Có hàm onlyOwner: Có`.

- Giữ `mint()` dòng 18–20 là quyền đặc biệt của `ClubTokenB`.

- Với `ClubTokenC`, xác định quyền đặc biệt là:
  `setRestricted(address user, bool status)` tại dòng 30–32.

- Ghi `_update()` dòng 34–36 là cơ chế thực thi việc hạn chế, không ghi đây là một quyền riêng của owner.

- Sửa mô tả rủi ro của `ClubTokenC` thành:
  "Owner có thể đánh dấu một địa chỉ là restricted, khiến địa chỉ đó không thể chuyển token đi."

**Ai phát hiện:** Sinh viên phát hiện khi đối chiếu lại kết quả AI với mã nguồn `ClubTokens.sol`.

## So sánh đọc thủ công và AI

### Sinh viên tự đọc tìm ra gì?

- Với `ClubTokenA`, tôi nhận thấy hợp đồng không kế thừa `Ownable` và không có `onlyOwner`, nhưng ban đầu chưa hiểu đầy đủ ý nghĩa về rủi ro.
- Với `ClubTokenB`, tôi nhận thấy có hàm `mint()`, nhưng ban đầu đọc nhầm và không nhận ra hàm này có `onlyOwner`. Tôi cũng chưa xác định được rủi ro của quyền mint.
- Với `ClubTokenC`, tôi nhận ra có `Ownable`, `onlyOwner`, hàm `setRestricted()` và `_update()`, nhưng chưa hiểu đầy đủ cách hai hàm này liên kết với nhau để hạn chế địa chỉ.

### AI tìm thêm được gì?

- AI giúp chỉ ra rằng `mint()` của `ClubTokenB` cho phép owner tạo thêm token mà mã nguồn không đặt giới hạn số lượng, từ đó có thể làm tăng tổng cung và gây pha loãng.
- AI giúp giải thích mối liên hệ giữa `setRestricted()` và `_update()` trong `ClubTokenC`: owner đặt trạng thái restricted, sau đó `_update()` kiểm tra trạng thái này để chặn việc chuyển token đi.
- AI giúp tôi hiểu rõ hơn sự khác nhau giữa quyền đặc biệt của owner và hàm nội bộ dùng để thực thi quyền đó.

### AI có nói sai chỗ nào không?

AI không phát hiện hàm không tồn tại trong mã nguồn và các hàm chính được nêu đều đúng.

Tuy nhiên, mô tả "ngăn chặn giao dịch" đối với `ClubTokenC` chưa đủ chính xác. Sau khi kiểm tra lại dòng 35, tôi sửa thành "ngăn địa chỉ bị restricted chuyển token đi".