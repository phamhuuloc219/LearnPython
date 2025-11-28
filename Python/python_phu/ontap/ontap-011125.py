a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
ucln = 1
so_nho_nhat = min(a, b) # Tìm số nhỏ nhất trong hai số a và b
    
for i in range (1, so_nho_nhat+1):
    if a % i == 0 and b % i == 0:
        ucln = i
print("Ước chung lớn nhất của", a, "và", b, "là:", ucln)

# if a > b:
#     for i in range (1, b+1):
#         if a % i == 0 and b % i == 0:
#             ucln = i
# else:
#     for i in range (1, a+1):
#         if a % i == 0 and b % i == 0:
#             ucln = i


n = int(input("Nhập n="))
dem = 0

while n < 0: # Nếu n âm thì nhập lại
    n = int(input("Nhập lại n: "))
    
while n > 0: # Nếu n = 0 thì không có chữ số
    n = n // 10 #
    dem += 1
    
print("Số chữ số của n là:", dem)