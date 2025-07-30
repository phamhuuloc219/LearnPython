# if <Điều kiện>:
#     <khối lệnh 1>
# else:
#     <khối lệnh 2>

# Viết chương trình kiểm tra mật khẩu và in ra "Mật khẩu đúng" nếu mật khẩu
# là "python", ngược lại in ra "Mật khẩu sai".

mat_khau = input("Nhập mật khẩu của bạn: ")
password = "python"


if (mat_khau == password):
    print("Mật khẩu đúng")
    print("Chúc mừng")
else:
    print("Mật khẩu sai") 
# print("Goodbye")

# # Viết chương trình yêu cầu người dùng nhập vào số đại diện cho ngày trong tuần (1-7).
# # Kiểm tra và in ra thông điệp tương ứng với ngày đó (1: Chủ nhật, 2: Thứ hai,...,7: Thứ bảy)
ngay_trong_tuan = int(input("Nhập ngày trong tuần (1-7): "))

if ngay_trong_tuan == 1:
    print("Chủ nhật")
elif ngay_trong_tuan == 2: # elif = else if = ngược lại nếu
    print("Thứ hai")
elif ngay_trong_tuan == 3:
    print("Thứ ba")
elif ngay_trong_tuan == 4:
    print("Thứ tư")
elif ngay_trong_tuan == 5:
    print("Thứ năm")
elif ngay_trong_tuan == 6:
    print("Thứ sáu")
elif ngay_trong_tuan == 7:
    print("Thứ bảy")
else: # ngược lại với tất cả những trường hợp đã liệt kê ở trên
    print("Số nhập vào không hợp lệ")
   





    
# Viết chương trình nhập vào 1 số nguyên n. Kiểm tra số đó là số chẵn hay lẻ
n = int(input("Nhập một số nguyên: "))
if n % 2 == 0: # kiểm tra số chẵn
    print("Số chẵn")
if n % 2 != 0: # kiểm tra số lẻ
    print("Số lẻ")
