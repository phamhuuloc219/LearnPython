# 1. Viết chương trình sử dụng vòng lặp while nhập 1 số nguyên dương n.
# n = int(input("Nhập 1 số nguyên dương: "))
# while n < 0:
#     n = int(input("Hãy nhập 1 số nguyên dương: "))
# print("Bạn đã nhập số nguyên dương: ",n)

# # 2. Viết chương trình sử dụng vòng lặp while nhập 1 số nguyên dương n và
# # tính tổng của các số từ 1 đến n.
# n = int(input("Nhập 1 số nguyên dương: "))
# while n < 0:
#     n = int(input("Hãy nhập 1 số nguyên dương: "))
# tong = 0
# for i in range(1, n+1):
#     tong += i
# print("Tong cac so tu 1 den", n, "la: ", tong)
# # 3. Viết chương trình sử dụng vòng lặp while tính tổng các chữ số của một số nguyên dương.
n = int(input("Nhập số nguyên dương n= "))
m = n % 10
tong_chu = 0
while n <= 0:
    n = int(input("Nhập lại số nguyên dương n= "))
while n > 0:
    tong_chu += n % 10
    n = n // 10
print(f"tổng chữ của {m} = {tong_chu}")  
# # 4. Viết chương trình nhập vào 1 số nguyên dương và kiểm tra số chẵn hay lẻ.
# n = int(input("Nhập 1 số nguyên dương: "))
# while n < 0:
#     n = int(input("Hãy nhập 1 số nguyên dương: "))
# if n % 2 == 0:
#     print("Số chẵn")
# else:
#     print("số lẻ")
# 5. Viết chương trình nhập vào điểm Toán, Tiếng Anh và Tiếng Việt
# và tính điểm trung bình.
# Giỏi (DTB >= 8 and DTB <=10)
# Khá (DTB >= 6.5 and DTB < 8)
# Trung Bình (DTB >= 5 and DTB < 6.5)
# Yếu (DTB >=0 and DTB < 5 )

# # Cách 1:
# diemToan = float(input("Bạn hãy nhập điểm Toán: "))
# diemTA = float(input("Bạn hãy nhập điểm Tiếng Anh: "))
# diemTV = float(input("Bạn hãy nhập điểm Tiếng Việt: "))
# while ((diemToan < 0 or diemToan >10) or (diemTA < 0 or diemTA >10) or (diemTV < 0 or diemTV >10)):
#     print("Điểm chỉ được nhập trong khoảng từ 0 đến 10 !!!")
#     diemToan = float(input("Bạn hãy nhập lại điểm Toán: "))
#     diemTA = float(input("Bạn hãy nhập lại điểm Tiếng Anh: "))
#     diemTV = float(input("Bạn hãy nhập lạilại điểm Tiếng Việt: "))

# diemTB = (diemToan + diemTA + diemTV) / 3
# print("Điểm trung bình của bạn là:", diemTB)

# if diemTB >= 8 and diemTB <= 10:
#     print("Bạn xếp loại: Giỏi")
# elif diemTB >= 6.5 and diemTB < 8:
#     print("Bạn xếp loại: Khá")
# elif diemTB >= 5 and diemTB < 6.5:
#     print("Bạn xếp loại: Trung Bình")
# elif diemTB >= 0 and diemTB < 5:
#     print("Bạn xếp loại: Yếu")
# else:
#     print("Không thấy vui trong lòng 😭")

# Cách 2:
diemToan = float(input("Bạn hãy nhập điểm Toán: "))
while (diemToan < 0 or diemToan >10):
    print("Điểm chỉ được nhập trong khoảng từ 0 đến 10 !!!")
    diemToan = float(input("Bạn hãy nhập lại điểm Toán: "))
    
diemTA = float(input("Bạn hãy nhập điểm Tiếng Anh: "))
while (diemTA < 0 or diemTA >10):
    print("Điểm chỉ được nhập trong khoảng từ 0 đến 10 !!!")
    diemTA = float(input("Bạn hãy nhập lại điểm Tiếng Anh: "))
    
diemTV = float(input("Bạn hãy nhập điểm Tiếng Việt: "))
while (diemTV < 0 or diemTV >10):
    print("Điểm chỉ được nhập trong khoảng từ 0 đến 10 !!!")
    diemTV = float(input("Bạn hãy nhập lạilại điểm Tiếng Việt: "))
    
diemTB = (diemToan + diemTA + diemTV) / 3
print("Điểm trung bình của bạn là:", diemTB)

if diemTB >= 8 and diemTB <= 10:
    print("Bạn xếp loại: Giỏi")
elif diemTB >= 6.5 and diemTB < 8:
    print("Bạn xếp loại: Khá")
elif diemTB >= 5 and diemTB < 6.5:
    print("Bạn xếp loại: Trung Bình")
elif diemTB >= 0 and diemTB < 5:
    print("Bạn xếp loại: Yếu")
else:
    print("Không thấy vui trong lòng 😭")