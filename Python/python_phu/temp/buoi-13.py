# 1. Viết chương trình nhập vào số nguyên dương n. 
# Tìm các số chia hết cho 3 và 5 trong khoảng từ 1 đến n

# if (i%3==0) and (i%5==0):
#     print(i)


# 2. Viết chương trình tính giá trị của biểu thức S= 1.2 + 2.3 + 3.4 + ... + n(n+1).
# n = int(input()) #5
# tong = 0
# for i in range(1,n+1):
#     # tong = tong + i*(i+1)
#     tong += i*(i+1)
# print(tong)

# 3. Viết chương trình tính tiền lương khi làm qua số giờ tiêu chuẩn theo quy định của công ty (tăng ca) của
# 1 nhân viên. Biết số giờ tiêu chuẩn là 44 giờ, lương theo giờ là 25$/h. Nếu làm tăng ca thì tính 30$/h. 
# Hãy tính số lương thực lãnh của nhân viên. Gợi ý: Đầu vào là 1 số lớn hơn hoặc bằng 44 
gio_tc = 44
luong_tc = 25
luong_tang_ca = 30
gio_lam = float(input("Nhập số giờ làm: "))

while gio_lam < gio_tc :
    gio_lam = float(input("Nhập lại số giờ làm >= 44 : "))
    
tong_luong = 0
gio_tang_ca = gio_lam - gio_tc
if gio_lam > gio_tc :
     tong_luong = gio_tc*luong_tc + gio_tang_ca*luong_tang_ca
else:
    tong_luong = gio_tc*luong_tc
# 4. Viết chương trình yêu cầu người dùng nhập vào số đại diện cho ngày trong tuần (1-7).
# Kiểm tra và in ra thông điệp tương ứng với ngày đó 
# (1: Chủ nhật, 2: Thứ hai,...,7: Thứ bảy)

# number = int(input("Nhâp 1 số đại diện cho ngày trong tuần: "))

# if number == 1:
#     print("Chủ nhật")
# elif number == 2:
#     print("Thứ Hai")
# elif number == 3:
#     print("Thứ Ba")
# elif number == 4:
#     print("Thứ Tư")
# elif number == 5:
#     print("Thứ Năm")
# elif number == 6:
#     print("Thứ Sáu")
# elif number == 7:
#     print("Thứ Bảy")
# else:
#     print("Bye")



# if <Điều kiện>:
#     <Thực hiện hành động 1>
# elif <Điều kiện2>:
#     <Thực hiện hành động 2>
# else:
#     <Thực hiện hành động 3>

# s = "xin chào các bạn"
# # for <Biến lặp> in <Chuỗi lặp>:
# for i in s:
#     print(i)
    
# for i in range(10):
#     print(i)
    
    
# for i in range(1,10):
#     for j in range(1,10):
#         print(i*j)