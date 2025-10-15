# 1. Viết chương trình máy tính cầm tay
# Gợi ý: cho người dùng nhập vào 2 số a, b và phép tính: + - x /
# - Nếu phép tính là + thì thực hiện phép + 2 số
# - Nếu phép tính là - thì thực hiện phép - 2 số
# - Nếu phép tính là x thì thực hiện phép x 2 số
# - Nếu phép tính là / thì thực hiện phép / 2 số
# + Ở phép chia nếu số b KHÁC 0 thì mới thực hiện phép chia
# a = int(input("Nhập số a= "))
# b = int(input("Nhập số b= "))
# phep_tinh = input("Nhập phép tính (+ - * /): ")
# ket_qua = 0
# if phep_tinh == "+":
#     ket_qua = a + b
#     print("Kết quả của phép cộng:", ket_qua)
# elif phep_tinh == "-":
#     ket_qua = a - b
#     print("Kết quả của phép trừ:", ket_qua)
# elif phep_tinh == "*":
#     ket_qua = a * b
#     print("Kết quả của phép nhân:", ket_qua)
# elif phep_tinh == "/" and b != 0:
#     ket_qua = a / b
#     print("Kết quả của phép chia:", ket_qua)
# else:
#     print("Error: Invalid")

# 2. Viết chương trình chuyển đổi tiền tệ với đầu vào là số tiền
# và đơn vị tiền tệ. ( Ví dụ: 20USD =492,299 VND; 100 EURO = 2,648,255 VND)
# usd = 25346.49
# euro = 26773
# franc = 28769.55

# money = float(input("Nhập số tiền bạn muốn quy đổi: "))
# unit = input("Nhập đơn vị tiền tệ: ")

# if  unit == "USD":
#     result = money * usd
# elif unit == "EURO":
#     result = money * euro
# elif unit == "FRANC":
#     result = money * franc
# else:
#     print("Loại tiền tệ này chưa được hỗ trợ !")

# print("Số tiền bạn quy đổi được là:", result,"VND")


#for bien_lap in chuoi_lap:
    #Khoi lenh trong For
    
# number = [3,6,3,7,2,4,9]
# for i in number:
#     print(i)

# Tính tổng các phần tử có trong danh sách
# number = [3,6,3,7,2,4,9]
# tong = 0
# for i in number:
#     tong = tong + i
    
# print("Tổng các phần tử có trong danh sách", tong)

for i in range(1,11):
    print(i)
    
tong = 0
for i in range(1,101):
    tong = tong + i
print("Tổng từ 1 đến 100 là:", tong)

#3. Viết chương trình sử dụng vòng lặp for để in ra các số chẵn từ 1 đến 20.
for i in range(1,21):
    if i % 2 == 0:
        print(i)
#4. Viết chương trình sử dụng vòng lặp for để in ra các phần tử của danh sách sau:
# ['apple', 'banana', 'cherry', 'date'].
tat_ca = ['apple', 'banana', 'cherry', 'date']
for x in tat_ca:
    print(x)