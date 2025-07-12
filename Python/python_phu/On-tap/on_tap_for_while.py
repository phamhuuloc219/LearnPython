# 1. Viết chương trình in bảng cửu chương từ 2 đến 9.
for i in range(2, 10):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
        
# 2. Viết chương trình cho người dùng đoán một số bí mật
# (dùng hàm random trong khoảng từ 10-99). Cho phép đoán đến khi đúng thì dừng.
import random
# dùng hàm randint để cho ra 1 số bất kỳ trong khoảng từ 10-99
so_bi_mat = random.randint(10, 99)
print("hãy nhập số bất kỳ")
so = int(input("Nhập số bí mật: "))
while so != so_bi_mat:
    print("Số bạn nhập Không phải là số bí mật")
    so = int(input("Nhập lại số bí mật: "))
print("Chúc mừng bạn đã nhập đúng số bí mật") 
   
# 3. Viết chương trình đếm có bao nhiêu số nguyên tố từ 1 đến n.
n = int(input("Nhập n = "))
dem = 0
for i in range(2, n+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i, end=" ") # end=" " để in các số trên cùng 1 dòng
        dem += 1
print("\nCác số nguyên tố từ 1 đến",n,"là: ", dem)

# 4. Giả sử mật khẩu đúng là "xuanphu". Yêu cầu người dùng nhập lại cho đến khi đúng. 
# Sau đó, in ra số lần đã nhập sai.
pass_word = "xuanphu"
mat_khau = input("Nhap mat khau: ").lower()
dem = 0
while mat_khau != pass_word:
    dem += 1
    print(f"Bạn nhập mật khẩu sai {dem} lần")
    mat_khau = input("Nhap lai mat khau: ").lower()
print("Mật khẩu đúng")
print(f"Bạn nhập mật khẩu sai {dem} lần")

# 5. Giả sử mật khẩu đúng là "xuanphu". Yêu cầu người dùng nhập lại cho đến khi đúng. 
# Nếu người dùng nhập sai 5 lần thì thoát chương trình
pass_word = "xuanphu"
mat_khau = input("Nhap mat khau: ").lower()
dem = 0
while mat_khau != pass_word:
    dem += 1
    if dem == 5:
        print(f"Bạn nhập mật khẩu sai {dem} lần")
        print("=======================================")
        print("Chương trình ngừng tại đây")
        break
    else:
        print(f"Bạn nhập mật khẩu sai {dem} lần")
        mat_khau = input("Nhap lai mat khau: ").lower()
        
if mat_khau == pass_word:
    print("=======================================")
    print("Chúc mừng bạn đã nhập đúng mật khẩu")