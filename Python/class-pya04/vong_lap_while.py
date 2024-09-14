# # # a = 1
# # # while a <= 10:
# # #     if a == 5:
# # #         a += 1
# # #         print("hello")
# # #     print(a)
# # #     a += 1
    
# # # a = 5
# # # while a != 0:
# # #     print(a)
# # #     a -= 2
# # b = 10
# # while b >= 1:
# #     print(b)
# #     b -= 1
# # else :
# #     print("end")
# """

# 2. Viết chương trình sử dụng vòng lặp while 
# nhập 1 số nguyên dương n.
# 3. Viết chương trình sử dụng vòng lặp while
# tính tổng của các số từ 1 đến n.




# 4. Viết chương trình tính tổng các chữ số
# của một số nguyên dương n nhập từ người dùng.
#     """
# n = int(input("Nhập số nguyên dương n (n>0): "))
# # kiem tra dau vao co lonn hon 0 ?
# while n < 0 :
#     n = int(input("Nhập lai số nguyên dương n (n>0): "))
    
# # khoi tao bien tong
# tong = 0
# # vong lap while tinh tong tu 1 den n
# while n >= 1 :
#     # tinh tong tu 1 den n
#     tong += n
#     n -= 1
# # in tong
# print(tong)

# Functions
def leap_year(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

#-------------------------------------------------------------
def valid_date(d, m, y):
    if d <= 0 or m <= 0 or m > 12 or y <= 0:
        return False
    if m == 2:
        if leap_year(y):
            return d in range(1, 30)  # 1 to 29 inclusive
        else:
            return d in range(1, 29)  # 1 to 28 inclusive
    elif m in [4, 6, 9, 11]:
        return d in range(1, 31)  # 1 to 30 inclusive
    else:
        return d in range(1, 32)  # 1 to 31 inclusive

#-------------------------------------------------------------
def next_day(d, m, y):
    if m == 2:
        if leap_year(y):
            d, m = (1, 3) if d == 29 else (d + 1, m)
        else:
            d, m = (1, 3) if d == 28 else (d + 1, m)
    elif m in [4, 6, 9, 11]:
        d, m = (1, m + 1) if d == 30 else (d + 1, m)
    else:
        if d == 31:
            if m == 12:
                d, m, y = 1, 1, y + 1
            else:
                d, m = 1, m + 1
        else:
            d += 1
    return d, m, y

#=======================================================================
# Main
str_day = input("Day/Month/Year: ")
a, b, c = map(int, str_day.split("/"))
if valid_date(a, b, c):
    x, y, z = next_day(a, b, c)
    print(f"Next date: {x}/{y}/{z}")
else:
    print("Invalid Date, Please Try Again.")
