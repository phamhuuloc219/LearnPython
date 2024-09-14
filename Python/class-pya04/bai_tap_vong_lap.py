# 1. Viết chương trình nhập số nguyên dương n. Tính tổng chữ số của n (Ví dụ: n = 123 => tong_chu_so = 6)
n = int(input("Nhập số nguyên dương n: "))
tong_chu_so = 0
while n > 0:
    tong_chu_so += n % 10  # Lấy chữ số cuối
    n //= 10  # Bỏ chữ số cuối
print(f"Tổng các chữ số là: {tong_chu_so}")

# 2. Viết chương trình nhập số nguyên dương n. Nếu trong khoảng từ 1-n có một số chia hết cho 3 và 5
# thì in ra màn hình số đó và ngược lại nếu không có số nào chia hết cho 3 và 5 
# thì in ra màn hình "Không có số nào chia hết cho 3 và 5 trong khoảng từ 1-n"
n = int(input("Nhập số nguyên dương n: "))
i = 1
found = False
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        found = True
    i += 1
if not found:
    print(f"Không có số nào chia hết cho 3 và 5 trong khoảng từ 1 đến {n}")

# 3. Viết chương trình nhập vào hai số nguyên dương n và k. Sử dụng vòng lặp while 
# để đếm và in ra số lượng các số từ 1 đến n chia hết cho k
n = int(input("Nhập số nguyên dương n: "))
k = int(input("Nhập số nguyên dương k: "))
i = 1
count = 0
while i <= n:
    if i % k == 0:
        count += 1
    i += 1
print(f"Số lượng các số từ 1 đến {n} chia hết cho {k} là: {count}")


# 4. Viết chương trình nhập vào số nguyên dương n. In ra màn hình 
# kết quả đảo ngược của số đó (Ví dụ: 123456 => 654321)
n = int(input("Nhập số nguyên dương n: "))
dao_nguoc = 0
while n > 0:
    dao_nguoc = dao_nguoc * 10 + n % 10  # Thêm chữ số cuối vào kết quả
    n //= 10  # Bỏ chữ số cuối
print(f"Số đảo ngược là: {dao_nguoc}")

# 5. Viết chương trình nhập vào số nguyên dương n. Kiểm tra xem n có phải là đối xứng hay không
# (Ví dụ: 12321 => là số đối xứng; 123 => là số không đối xứng)
n = int(input("Nhập số nguyên dương n: "))
original = n
dao_nguoc = 0
while n > 0:
    dao_nguoc = dao_nguoc * 10 + n % 10  # Tạo số đảo ngược
    n //= 10  # Bỏ chữ số cuối
if original == dao_nguoc:
    print(f"{original} là số đối xứng")
else:
    print(f"{original} không phải là số đối xứng")

###################################################################################################

# 1. Tìm ước số chung lớn nhất (ƯCLN) của hai số nguyên dương a và b
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

ucln = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        ucln = i
print(f"Ước số chung lớn nhất của {a} và {b} là: {ucln}")

# 2.
n = int(input("Nhập số nguyên: "))
dao_nguoc = 0
for digit in str(n):
    dao_nguoc = int(digit) + dao_nguoc * 10
print(f"Số đảo ngược là: {dao_nguoc}")

# 3.
n = int(input("Nhập số nguyên dương n: "))
a, b = 0, 1
fibonacci = []
for i in range(n):
    fibonacci.append(a)
    a, b = b, a + b
print(f"{n} phần tử đầu tiên của dãy Fibonacci: {fibonacci}")

# def fibonacci(n):
#     f0 = 0
#     f1 = 1
#     fn = 1
 
#     if (n < 0):
#         return -1
#     elif (n == 0 or n == 1):
#         return n
#     else:
#         for i in range(2, n):
#             f0 = f1
#             f1 = fn
#             fn = f0 + f1
#         return fn
    
# n = int(input("Nhap so phan tu cua day fibonaci: "))
# print(f"{n} số đầu tiên của dãy số fibonacci: ")

# sb = ""
# for i in range(0, n):
#     sb = sb + str(fibonacci(i)) + ", "
# print(sb)

# 4.
n = int(input("Nhập số nguyên dương n: "))
a, b = 0, 1
fibonacci = []
for i in range(n + 1):
    if a > n:
        break
    fibonacci.append(a)
    a, b = b, a + b
print(f"Các phần tử của dãy Fibonacci từ 0 đến {n}: {fibonacci}")

# f0 = 0
# f1 = 1
# n = int(input("Nhap so phan tu trong day fibo: "))

# print(f"{f0} {f1} ", end="")
# for i in range (1,n):
#     fn = f0 + f1
#     print(fn,end=" ")
#     f0 = f1
#     f1 = fn

# 5. Vẽ tam giác "*" có chiều cao n hàng
n = int(input("Nhập số nguyên dương n: "))
for i in range(1, n + 1):
    print("*" * i)
    
# 6. Tính biểu thức S = 1 + 1/2^3 + 1/3^3 + ... + 1/n^3 (làm tròn 5 chữ số thập phân)
n = int(input("Nhập số nguyên dương n: "))
S = 0
for i in range(1, n + 1):
    S += 1 / i**3
print(f"Giá trị của S là: {round(S, 5)}")

# 7. Tính tổng bình phương các số từ x đến y
x = int(input("Nhập số nguyên x: "))
y = int(input("Nhập số nguyên y: "))
S = 0
for i in range(x, y + 1):
    S += i ** 2
print(f"Tổng bình phương các số từ {x} đến {y} là: {S}")

# 8. Kiểm tra số n có phải là số hoàn hảo hay không
n = int(input("Nhập số nguyên dương n: "))
tong_uoc = 0
for i in range(1, n):
    if n % i == 0:
        tong_uoc += i
if tong_uoc == n:
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không phải là số hoàn hảo")

# 9. Tìm tổng của tất cả các số lẻ và chẵn nằm giữa hai số a và b
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

tong_chan = 0
tong_le = 0
for i in range(min(a, b), max(a, b) + 1):
    if i % 2 == 0:
        tong_chan += i
    else:
        tong_le += i

print(f"Tổng các số chẵn giữa {a} và {b} là: {tong_chan}")
print(f"Tổng các số lẻ giữa {a} và {b} là: {tong_le}")

# 10. Tính giá trị biểu thức S = 1.2 + 2.3 + 3.4 + ... + n(n+1)
n = int(input("Nhập số nguyên dương n: "))
S = 0
for i in range(1, n + 1):
    S += i * (i + 1)
print(f"Giá trị của biểu thức S là: {S}")