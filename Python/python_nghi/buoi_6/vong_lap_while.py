# Nhập 1 số nguyên dương. Nếu khong phải là số nguyên dương thì
# yêu cầu người dùng nhập lại.
n = int(input("Nhập n = "))

while n < 0:
    print("Số bạn vừa nhập là: ", n)
    n = int(input("Nhập lại n = "))
    
print("Số bạn vừa nhập là: ", n)
print("Xong")

# bài 1
mat_khau = "python"
password = input("Nhap mat khau: ")
while mat_khau != password:
    print("Sai mat khau")
    password = input("Nhap lai mat khau: ")
print("Dung mat khau")

# bài 2
...