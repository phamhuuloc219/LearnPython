# a = 1
# while a <=10:
#     print(a, end=" ")
#     a += 1
    
# 3. Viết chương trình sử dụng vòng lặp while tính tổng của các số từ 1 đến 100.
# 4. Viết chương trình tính tổng các chữ số của một số nguyên dương n nhập từ người dùng.
# n = int(input("Nhập số nguyên dương n= "))
# m = n % 10
# tong_chu = 0
# while n <= 0:
#     n = int(input("Nhập lại số nguyên dương n= "))
# while n > 0:
#     tong_chu += n % 10
#     n = n // 10
# print(f"tổng chữ của {m} = {tong_chu}")   
# 5. Viết chương trình đảo ngược các chữ số của một số nguyên dương n nhập từ người dùng.
n = int(input("Nhập số nguyên dương n= "))
m = n
dao_nguoc = 0
while n <= 0:
    n = int(input("Nhập lại số nguyên dương n= "))
while n > 0:
    dao_nguoc = dao_nguoc * 10 + n % 10
    n = n // 10
print(f"so dao nguoc của {m} = {dao_nguoc}") 