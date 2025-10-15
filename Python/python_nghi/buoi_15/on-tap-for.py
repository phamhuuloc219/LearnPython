# 1. Viết chương trình sử dụng vòng lặp for để tìm ước số chung lớn nhất (ƯCLN)
# của hai số nguyên dương a và b.

# a = int(input("Nhập số a= "))
# b = int(input("Nhập số b= "))
# ucln = 1
# min_number = 0

# if a > b: # tìm số nhỏ nhất
#     min_number = b
# else:
#     min_number = a
    
# for i in range(1, min_number+1):
#     if a % i == 0 and b % i == 0:
#         ucln = i
            
# print(f"Ước chung lớn nhất của {a} và {b} là {ucln}")

# 2.Viết chương trình nhập một số nguyên và in kết quả ra
# màn hình dưới dạng số đảo ngược (về thứ tự) của số nguyên vừa nhập đó.
n = int(input("Nhập vào 1 số: "))
str1 = str(n)
str_reverse = ""

for i in range(len(str1)-1 , -1, -1):
    str_reverse += str1[i]
    
result = int(str_reverse)
print(result)

# Đảo ngược chuỗi
str2 = input("Nhập vào 1 chuỗi: ")
str_reverse2 = ""

for i in range(len(str2)-1 , -1, -1):
    str_reverse2 += str2[i]

print(str_reverse2)