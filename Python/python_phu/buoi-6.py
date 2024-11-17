# # and => tất cả điều kiện đều phải đúng thì mới thực hiện đoạn lệnh
# if (5<6 and 6<7 and 3<9 and 5<10):
#     print("yeahskhdasd")
# else:
#     print("no")
# # or => chỉ cần 1 cái đúng thì sẽ thực hiện đoạn lệnh
# if (5<6 or 6<7 or 3<9 or 5<10):
#     print("yeahskhdasd")
# else:
#     print("no")

# Bài 1
# Viết chương trình kiểm tra mật khẩu và in ra "Mật khẩu đúng"
# nếu mật khẩu là "python", ngược lại in ra "Mật khẩu sai".
# password = "python"
# nhap_mat_khau = input("Enter your password: ")

# # Cách 1:
# if (nhap_mat_khau == password):
#     print("Mật khẩu đúng")
# if (nhap_mat_khau != password):
#     print("Mật khẩu sai")
    
# # Cách 2:
# if (nhap_mat_khau == password):
#     print("Mật khẩu đúng")
# else:
#     print("Mật khẩu sai") 

# Bài 2
# Viết chương trình yêu cầu người dùng nhập vào số đại diện cho ngày trong tuần (1-7).
# Kiểm tra và in ra thông điệp tương ứng với ngày đó (1: Chủ nhật, 2: Thứ hai,...,7: Thứ bảy)
# days = int(input("Nhập số đại diện cho ngày trong tuần: "))

# if (days == 1):
#     print("Chủ nhật")
# elif (days == 2):
#     print("Thứ hai")
# elif (days == 3):
#     print("Thứ ba")
# elif (days == 4):
#     print("Thứ tư")
# elif (days == 5):
#     print("Thứ năm")
# elif (days == 6):
#     print("Thứ sáu")
# elif (days == 7):
#     print("Thứ bảy")
# else:
#     print("Số nhập vào không đúng vui lòng nhập 1 số trong khoảng từ 1-7 !!!")
# Bài 3
# Viết chương trình yêu cầu người dùng nhập vào giờ (24 giờ).
# Kiểm tra và in ra thông điệp dựa trên giờ: buổi sáng (5-11 giờ),
# buổi chiều (12-17 giờ), buổi tối (18-22 giờ), ban đêm (23-4 giờ).

# time = int(input("Nhập vào giờ (24 giờ): "))

# if (time >= 5 and time <= 11):
#     print("buổi sáng")
# elif (time >= 12 and time <= 17):
#     print("buổi chiều")
# elif (time >= 18 and time <= 22):
#     print("buổi tối")
# elif ((time == 23) or (time >= 0 and time <= 4)):
#     print("ban đêm")
# else:
#     print("Số nhập vào không đúng vui lòng nhập giờ trong khoảng từ 0-23!!!")


# Cấu trúc if-elif-else
"""
    elif = else if
    
if <Điều kiện>:
    <Thực hiện hành động 1>
elif <Điều kiện2>:
    <Thực hiện hành động 2>
elif <Điều kiện3>:
    <Thực hiện hành động 3>
elif <Điều kiện4>:
    <Thực hiện hành động 4>
elif <Điều kiện5>:
    <Thực hiện hành động 5>
else:
    <Thực hiện hành động 6>
    
"""

# Viết chương trình nhập vào điểm của học sinh và
# xếp hạng học lực của học sinh dựa trên:
# - Điểm trung bình >= 9.0 và < 10 là Xuất sắc.
# - Điểm trung bình >=7.0 và < 9.0 là Giỏi
# - Điểm trung bình >5.0 và < 7.0 là Khá
# - Điểm trung bình >=3.5 và <= 5.0 là Trung Bình
# - Điểm trung bình <3.5 là Yếu

