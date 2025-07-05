# 1. Viết chương trình tính tổng các số chẵn trong khoảng từ 1 - n

# n = int(input("Nhap n: "))
# tong = 0 
# for i in range(1, n+1):
#     if (i % 2 == 0):
#         tong = tong + i

# 2. Viết chương trình kiểm tra mật khẩu. Nếu người dùng nhập vào mật khẩu
# là "python", in ra "Mật khẩu đúng".Ngược lại, thông báo "sai mật khẩu"
# và nhập mật khẩu cho đến khi có mật khẩu đúng.

# mat_khau = "python"
# password = input("Nhap mat khau: ").lower()
# while password != mat_khau:
#     print("Sai mat khau")
#     password = input("Nhap lai mat khau: ").lower()
# print("Dung mat khau")

# Viết chương trình tính tổng các số chẵn trong khoảng từ 5 - 99
# tong = 0
# for i in range(5, 100):
#     if (i % 2 == 0):
#         tong = tong + i

# print(tong)        


        

    


# 7. In dãy FizzBuzz từ 1 đến 50
# Với mỗi số:
# Nếu chia hết cho 3 in "Fizz"
# Nếu chia hết cho 5 in "Buzz"
# Nếu chia hết cho cả 3 và 5 in "FizzBuzz"
# Ngược lại in chính số đó 
# for i in range (1, 51):
#     if i % 3 == 0:
#         print ("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif (i % 3 == 0) and (i % 5 == 0):
#         print("FizzBuzz")
#     else:
#         print(i)
        
# 2. Viết chương trình tính giá trị của biểu thức S= 1.2 + 2.3 + 3.4 + ... + n(n+1).     
n = int(input("Nhập n = "))
s = 0
for i in range (1, n+1):
    s = s + i*(i+1)
print(s)