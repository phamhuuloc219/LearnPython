"""
Biến:
- Không được bắt đầu bằng số   vd: 4number= 4 => sai   
- Không bắt đầu bằng kí tự đặc biệt   vd: @ ! # $ % ^ & * ( ) [] {} / < > = - +
- Không được chưa khoảng trắng vd: so nguyen = 19
- tên biến có thể đặt bằng dấu "_": vd: _number = 2 => đúng 
- tên biến phải có nghĩa : vd number = 5 ; name = "loc" 
"""

# # Sử dụng biến để lưu giá trị, ví dụ:
# number = 10
# weight = 63.5
# name = "Loc"
# is_happy = True
# school = None
#  In giá trị của biến
# print(number)
# print(weight)
# print(name)
# print(is_happy)
# print(school)


# # Kiểm tra kiểu dữ liệu: dùng hàm type() để kiểm tra
# print(type(number)) # <class 'int'> => số nguyên
# print(type(weight)) # <class 'float'> => số thực
# print(type(name)) # <class 'str'> => chuỗi
# print(type(is_happy)) # <class 'bool'> => Đúng/Sai
# print(type(school)) # <class 'NoneType'> => None

# dùng input() để nhập dữ liệu từ bàn phím
# Cách 1:
# a = input("Nhập số a=") # => a="76"
# a = int(a) #=> a=76

# b = input("Nhập số b=") # => b="12"
# b = int(b) # => b=12

# Cách 2:
a = int(input("Nhập số a="))
b = int(input("Nhập số b="))


tong = a + b
print("tong 2 so = ",tong)
hieu = a - b
print("hieu 2 so = ",hieu)
tich = a * b
print("tich 2 so = ",tich)
thuong = a / b
print("thuong 2 so = ",thuong)