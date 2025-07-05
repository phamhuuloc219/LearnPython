# a = int(input("a= "))
# b = int(input("b= "))

# ucln = 1
#Cách 1: kiểm tra nếu số nào nhỏ hơn thì cho chạy
# 1 vòng lặp for từ 1 đến số đó
# if(a<b):
#     for i in range(1, a+1):
#         if( a % i == 0 and b % i == 0):
#             ucln = i
# else:
#     for i in range(1, b+1):
#         if( a % i == 0 and b % i == 0):
#             ucln = i

# Cách 2: dùng hàm min để kiểm tra số nhỏ nhất trong 2 số a và b
# for i in range(1, min(a,b)+1):
#         if( a % i == 0 and b % i == 0):
#             ucln = i
            
# print(f"UCLN cua {a} va {b} la: {ucln}")


# tìm trong khoảng từ a đến b có bao nhiêu số là số nguyên tố
a = int(input("a= "))
b = int(input("b= "))

so_nguyen_to = []
khong_phai_so_nguyen_to = []

for i in range(a, b +1):
    for num in range(2, i):
        if(i % num == 0):
            khong_phai_so_nguyen_to.append(i)
            break
    else: 
        so_nguyen_to.append(i)

print("Các số nguyên tố là: ",so_nguyen_to)
print("Các số không phải là số nguyên tố là: ",khong_phai_so_nguyen_to)
# print(f"Khoang {a} den {b} co {so_nguyen_to} so nguyen to va {khong_phai_so_nguyen_to} khong phai so nguyen to")