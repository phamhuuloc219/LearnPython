# # nhập dữ liệu từ bàn phím và gán vào trong biến

# # ép kiểu về kiểu số nguyên
# # cách 1:
# # diem = input("Nhập điểm: ")
# # diem = int(diem) 

# # cách 2:
# diem = int(input("Nhập điểm: "))

# print("Điểm vừa nhập là: ",diem) # in ra kết quả vừa nhập

# # nếu điểm lớn hơn 9 thì đạt danh hiệu học sinh xuất sắc
# if diem > 9:
#     print("Đạt danh hiệu học sinh xuất sắc")
# else:
#     print("Không đạt danh hiệu học sinh xuất sắc")






# Bài 1:
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
tong = a + b

if tong > 100:
    print("yay 🤩")
else:
    print("😡")
    
# 2. Viết chương trình kiểm tra 2 số a và b
# được nhập từ bàn phím. nếu số nào lớn hơn
# thì in ra màn hình số đó

# a = int(input("Nhập số thứ nhất: "))
# b = int(input("Nhập số thứ hai: "))
# phep_tinh = input("Nhập phép tính(+, -, *, /): ")

# ket_qua = 0

# if phep_tinh == "+" :
#     ket_qua = a + b
#     print("Kết quả: ",ket_qua)
# elif phep_tinh == "-" :
#     ket_qua = a - b
#     print("Kết quả: ",ket_qua)
# elif phep_tinh == "*" :
#     ket_qua = a * b
#     print("Kết quả: ",ket_qua)
# elif phep_tinh == "/":
#     if b != 0: # kí hiệu != có nghĩa là khác
#         ket_qua = a/b
#         print("Kết quả: ",ket_qua)
#     else: # b == 0:
#         print("Không thể chia với số 0")
# else:
#     print("Phép tính không hợp lệ")



gia_tri = float(input("Nhập giá trị: "))
don_vi_tien_te = input("Nhập đơn vị tiền tệ: ")
tien = 0

if don_vi_tien_te == "USD":
    tien = gia_tri * 26421
    print("Tổng số tiền sau khi quy đổi sang VNĐ là:",tien)
elif don_vi_tien_te == "EUR":
    tien = gia_tri * 30965
    print("Tổng số tiền sau khi quy đổi sang VNĐ là:",tien)
elif don_vi_tien_te == "RUB":
    tien = gia_tri * 318.1
    print("Tổng số tiền sau khi quy đổi sang VNĐ là:",tien)
# Có thể thêm nhiều loại tiền tệ
else: # Ngược lại với tất cả các trường hợp đã liệt kê ở trên
    print("Đơn vị tiền tệ không hợp lệ !!!")