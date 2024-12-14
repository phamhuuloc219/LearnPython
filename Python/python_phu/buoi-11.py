# 1. Viết chương trình sử dụng vòng lặp while nhập 1 số nguyên dương n.
# n = int(input("Nhập 1 số nguyên dương: "))
# while n < 0:
#     n = int(input("Hãy nhập 1 số nguyên dương: "))
# print("Bạn đã nhập số nguyên dương: ",n)

# 2. Viết chương trình sử dụng vòng lặp while nhập 1 số nguyên dương n và
# tính tổng của các số từ 1 đến n.
n = int(input("Nhập 1 số nguyên dương: "))
while n < 0:
    n = int(input("Hãy nhập 1 số nguyên dương: "))
tong = 0
for i in range(1, n+1):
    tong += i
print("Tong cac so tu 1 den", n, "la: ", tong)
# 3. Viết chương trình sử dụng vòng lặp while tính tổng các chữ số của một số nguyên dương.
# 4. Viết chương trình nhập vào 1 số nguyên dương và kiểm tra số chẵn hay lẻ.
n = int(input("Nhập 1 số nguyên dương: "))
while n < 0:
    n = int(input("Hãy nhập 1 số nguyên dương: "))
if n % 2 == 0:
    print("Số chẵn")
else:
    print("số lẻ")
# 5. Viết chương trình nhập vào điểm Toán, Tiếng Anh và Tiếng Việt
# và tính điểm trung bình.
# Giỏi (DTB >= 8 and DTB <=10)
# Khá (DTB >= 6.5 and DTB < 8)
# Trung Bình (DTB >= 5 and DTB < 6.5)
# Yếu (DTB >=0 and DTB < 5 )