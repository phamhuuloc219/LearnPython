# n = int(input("Nhập n = "))
# s = 0

# for i in range(1, n+1):
#     s += 1/(i**3)
# s = round(s, 2)
# print(s)

# 10. Nhập số nguyên n. 
# Tính giá trị biểu thức S= 1.2 + 2.3 + 3.4 + ... + n(n+1).
n = int(input("Nhập n = "))
s = 0

for i in range(1,n+1):
    s += i*(i+1)
print(s)

# 9. Nhập vào hai số nguyên dương a và b. 
# Tìm tổng của tất cả các số lẻ và chẵn nằm giữa hai số đó.
a = int(input("Nhập số a= "))
b = int(input("Nhập số b= "))
tong_chan = 0
tong_le = 0
for i in range(a+1, b):
    if ( i%2 == 0):
        tong_chan += i
    elif ( i%2 !=0):
        tong_le += i

print(f"Tổng các số lẻ trong khoảng từ {a} đến {b} là: {tong_le}")
print(f"Tổng các số chẵn trong khoảng từ  {a} đến {b} là: {tong_chan}")