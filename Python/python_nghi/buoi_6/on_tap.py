# 9. Nhập vào hai số nguyên dương a và b. 
# Tìm tổng của tất cả các số lẻ và chẵn nằm giữa hai số đó.

a = int(input("Nhap a="))
b = int(input("Nhap b="))

tong_chan = 0
tong_le = 0

for i in range(a+1, b):
    if i % 2 == 0:
        tong_chan = tong_chan + i
    else:
        tong_le = tong_le + i
        
print(f"Tong cac so le trong khoang tu {a} den {b} la: {tong_le}")
print(f"Tong cac so chan trong khoang tu {a} den {b} la: {tong_chan}")