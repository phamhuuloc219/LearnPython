# n = int(input("Enter the number: "))
# for i in range(1, 11):
#     print(n*i)
#     #Cách 1: 
#     print(f"{n} x {i} = {n * i}")
#     #Cách 2:
#     print(n, " x ", i, " = ", n*i)
  
# diemToan = int(input("Nhập điểm toán = "))
# while (diemToan < 0):
#     diemToan = int(input("Nhập lại điểm toán = "))


# str = input("Nhap chuoi: ")
# char = input("Nhap ki tu: ")
# dem = 0

# dem = str.count(char)

# for chars in str:
#     if chars == char:
#         dem += 1


# print("Xuat hien: ",dem)

str = input("Nhap chuoi: ")
str_new =""
for char in str:
    str_new = char + str_new
    
if str == str_new:
    print("Chuoi doi xung")
else:
    print("Chuoi khong doi xung")
