# Remembers
"""Bài tập: Viết một chương trình nhận một chuỗi từ người dùng và in ra độ dài của chuỗi đó.
Ví dụ: Chuỗi """"Hello, World!"""" có độ dài là 13.""""print(len(str))"""" 2 dòng
Giải:
        dòng 1: nhập vào từ bàn phím
    chuoi = input("Nhập vào 1 chuỗi ký tự: ")
        dòng 2: In ra số lượng ký tự có trong chuỗi vừa nhập bằng cách sử dụng hàm len()
    print(len(chuoi))

""

""Bài tập: Viết một chương trình nhận một chuỗi từ người dùng và in ra chuỗi đó với tất cả chữ cái là chữ hoa
và chữ thường.
Ví dụ: Chuỗi """"Python"""" -> """"PYTHON"""" và """"python"""". 4 dòng
Giải:
str = input("........")
Dòng 1 : chuỗi vừa nhập =>print(str)
Dòng 2 : chuỗi in hoa -> print(str.upper())
Dòng 3 : chuỗi in thường
""














""Bài tập: Viết một chương trình nhận một chuỗi từ người dùng và in ra chuỗi đó với tất cả chữ cái là chữ thường.
Ví dụ: Chuỗi """" Hello, World! """" -> """"Hello, World!"""".
""
Bài tập: Viết một chương trình nhận một chuỗi từ người dùng với các khoảng trắng ở đầu và cuối, và in ra chuỗi sau khi loại bỏ khoảng trắng.
Bài tập: Viết một chương trình nhận một chuỗi từ người dùng và thay thế tất cả các xuất hiện của một chuỗi con cụ thể bằng một chuỗi mới.
""Bài tập: Viết một chương trình nhận một chuỗi từ người dùng và tách chuỗi đó thành một danh sách các chuỗi con dựa trên một ký tự phân cách cụ thể.
Ví dụ: Chuỗi """"apple,banana,cherry"""" với ký tự phân cách """","""" -> [""""apple"""", """"banana"""", """"cherry""""].
""
Bài tập: Viết một chương trình nhận một danh sách các chuỗi từ người dùng và kết hợp chúng thành một chuỗi với một ký tự phân cách cụ thể.
""Bài tập: Viết một chương trình nhận một chuỗi từ người dùng và tìm vị trí của một chuỗi con trong chuỗi đó.
Ví dụ: Chuỗi """"Hello, World!"""" tìm vị trí của """"World"""" -> 7.
""
""Bài tập: Viết một chương trình nhận một chuỗi từ người dùng và kiểm tra xem chuỗi đó có bắt đầu bằng một chuỗi cụ thể và có kết thúc bằng một chuỗi cụ thể không.
Ví dụ: Chuỗi """"Python Programming"""" kiểm tra bắt đầu bằng """"Python"""" và kết thúc bằng """"Programming"""" -> True.
""
""Bài tập: Viết một chương trình nhận một chuỗi từ người dùng và kiểm tra xem chuỗi đó có phải là số không.
Ví dụ: Chuỗi """"12345"""" -> True, Chuỗi """"Hello"""" -> False.
"""

# Exercise
""""
Bài 1: Viết chương trình nhập một xâu kí tự từ bàn phím. Kết quả là 1 dãy kí tự của xâu này:
ví dụ:

Xâu nhập vào: Việt Nam
Kết quả ra: [""V"",""i"",""ệ"",""t"",""N"",""a"",""m""]
Bài 2: Viết chương trình khai báo các phần tử danh sách. Yêu cầu:
Xoá 1 phần tử theo vị trí bất kì(đầu danh sách, cuối danh sách, giữa danh sách)
Xoá các phần tử theo vị trí bắt đầu và kết thúc
Thêm mới 1 phần tử theo vị trí bất kì(đầu, giữa, cuối danh sách)
Thêm các phần tử theo vị trí bắt đầu và vị trí kết thúc chèn.
Bài 3: Nhập từ bàn phím họ tên người Việt Nam đầy đủ. Viết chương trình tách và in ra họ, đệm, tên của người đó.
Bài 4: Viết thủ tục convert() thực hiện các công việc sau:
Yêu cầu nhập từ bàn phím số giờ, phút, giây (tính theo số nguyên)
Đổi tổng số thời gian này ra ngày
Hiển thị kết quả ra màn hình"

"""





# Loại bỏ khoảng trắng ở 2 đầu chuỗi kí tự
# Cách sử dụng:
# - Tạo 1 biến mới => gọi lại biến lưu trữ giá trị của chuỗi
# Sau đó gọi hàm bằng cách .strip()

s = "    Xin Chào Các Bạn    "

s_new = s.strip() # loại bỏ khoảng trắng ở 2 đầu chuỗi ký tự
print(s_new)


# Cách sử dụng thực tế:
name = input("Nhập tên: ")
# Tạo biến mới để lưu kết quả sau khi loại bỏ khoảng
# trắng ở 2 đầu chuỗi ký tự
name_main = name.strip()
# in ra kết quả sau khi xử lý
print(name_main)