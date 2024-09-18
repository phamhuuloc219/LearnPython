# Bài tập buổi 18:
# 1. Hàm kiểm tra một số có phải là số nguyên tố không
def kiem_tra_so_nguyen_to(num):
    # # Kiểm tra số nhỏ hoặc bằng 1 không phải là số nguyên tố
    # if num <= 1:
    #     return False
    # # Kiểm tra số 2 và 3 là số nguyên tố
    # if num <= 3:
    #     return True
    # # Loại trừ số chia hết cho 2 hoặc số chia hết cho 3
    # if num % 2 == 0 or num % 3 == 0:
    #     return False
    # # Kiểm tra các số từ 5 đến căn bậc hai của num
    # i = 5
    # while i * i <= num:
    #     if num % i == 0 or num % (i + 2) == 0:
    #         return False
    #     i += 6
    # return True

    # Ban đầu đặt k = 1. Vòng lặp sẽ tăng k lên 1 đơn vị cho đến khi k = num thì dừng.
    #  Với mỗi k, kiểm tra nếu k là ước của num thì tăng dem_uoc lên 1
    # k = 1
    # dem_uoc = 0
    # while k < num:
    #     if num % k == 0:
    #         dem_uoc += 1
    #     k += 1  # k = k + 1
    # if dem_uoc == 1:
    #     return True
    # else:
    #     return False

    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# 2. Hàm xác định loại tam giác dựa trên độ dài ba cạnh (Phát)
def xac_dinh_tam_giac(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Độ dài các cạnh phải là số dương"

    # Kiểm tra xem ba cạnh có tạo thành tam giác hợp lệ không
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Tam giác đều"
        elif a == b or b == c or a == c:
            return "Tam giác cân"
        else:
            return "Tam giác thường"
    else:
        return "Ba cạnh không tạo thành tam giác"
# 3. Hàm kiểm tra tuổi để xác định có đủ điều kiện bầu cử hay không?


def kiem_tra_bau_cu(age):
    if age >= 18:
        return "Đủ điều kiện bầu cử"
    else:
        return "Không đủ điều kiện bầu cử"


# Ví dụ sử dụng
print(kiem_tra_bau_cu(20))  # Đủ điều kiện bầu cử
print(kiem_tra_bau_cu(16))  # Không đủ điều kiện bầu cử

# 4. Hàm tính tổng các số từ 1 đến n (Trọng)


def tong_tu_1_den_n(n):
    tong = 0
    for i in range(1, n + 1):
        tong += i
    return tong


# Ví dụ sử dụng
print(tong_tu_1_den_n(10))  # 55
print(tong_tu_1_den_n(5))   # 15

# 5. Hàm in ra các số chẵn từ 1 đến n


def in_so_chan(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, end=' ')
    print()


# Ví dụ sử dụng
in_so_chan(10)  # 2 4 6 8 10
in_so_chan(7)   # 2 4 6

# 6. Hàm in ra các số lẻ từ 1 đến n


def in_so_le(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, end=' ')
    print()


# Ví dụ sử dụng
in_so_le(10)  # 1 3 5 7 9
in_so_le(7)   # 1 3 5 7

# 7. Hàm tính tổng các số từ 1 đến n sử dụng vòng lặp while


def tong_tu_1_den_n_while(n):
    tong = 0
    i = 1
    while i <= n:
        tong += i
        i += 1
    return tong


# Ví dụ sử dụng
print(tong_tu_1_den_n_while(10))  # 55
print(tong_tu_1_den_n_while(5))   # 15

# 8. Hàm in ra các số chẵn từ 1 đến n sử dụng vòng lặp while


def in_so_chan_while(n):
    i = 1
    while i <= n:
        if i % 2 == 0:
            print(i, end=' ')
        i += 1
    print()


# Ví dụ sử dụng
in_so_chan_while(10)  # 2 4 6 8 10
in_so_chan_while(7)   # 2 4 6

# 9. Hàm in ra các số lẻ từ 1 đến n sử dụng vòng lặp while


def in_so_le_while(n):
    i = 1
    while i <= n:
        if i % 2 != 0:
            print(i, end=' ')
        i += 1
    print()


# Ví dụ sử dụng
in_so_le_while(10)  # 1 3 5 7 9
in_so_le_while(7)   # 1 3 5 7

# 10. Hàm in ra các số nguyên tố từ 1 đến n
n = int(input("Nhập số nguyên N: "))
for i in range(1, n+1):
    if kiem_tra_so_nguyen_to(i) == True:
        print(f"{i} là số nguyên tố")
    else:
        print(f"{i} không là số nguyên tố")
# 11. Hàm in ra dãy số Fibonacci từ 1 đến n


def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a != 0:  # Skip the initial 0
            print(a, end=' ')
        a, b = b, a + b
    print()


# Ví dụ sử dụng
fibonacci(10)  # 1 1 2 3 5 8
fibonacci(20)  # 1 1 2 3 5 8 13

# 12. Viết hàm tính UCLN của hai số nguyên nhập từ bàn phím và in ra màn hình


def ucln(a, b):
    while b:
        a, b = b, a % b
    return a


# Ví dụ sử dụng
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
print(f"UCLN của {a} và {b} là: {ucln(a, b)}")

# 13. Hàm in ra các số hoàn hảo từ 1 đến n sử dụng vòng lặp while


def is_perfect(num):
    if n <= 0:
        return False  # Số hoàn hảo phải là số dương

    tong_cac_uoc = 0  # Khởi tạo biến để tính tổng các ước số

    # Tìm các ước số của n, bắt đầu từ 1 đến n-1
    for i in range(1, n):
        if n % i == 0:
            tong_cac_uoc += i  # Cộng các ước số vào tổng

    # So sánh tổng các ước số với n
    return tong_cac_uoc == n


def in_so_hoan_hao(n):
    i = 1
    while i <= n:
        if is_perfect(i):
            print(i, end=' ')
        i += 1
    print()


# Ví dụ sử dụng
in_so_hoan_hao(10000)  # 6 28 496 8128
in_so_hoan_hao(1000)   # 6 28 496
