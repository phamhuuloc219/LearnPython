# 1. Viết chương trình tính kết quả biểu thức S= 1+1/2^3+1/3^3+...+1/n^3 (làm tròn 5 chữ số thập phân).
n = int(input("Nhập số n= "))
s = 0
for i in range(1, n+1):
    s = s + 1/pow(i, 3)
    
print("S= ", round(s, 5))

# 2. Nhập 2 số nguyên x và y. Viết chương trình tính tổng bình phương các số từ x đến y.
x = int(input("Nhập số x= "))
y = int(input("Nhập số y= "))
while x > y:
    x = int(input("Nhập số x= "))
s = 0
for i in range(x, y+1):
    s = s + pow(i, 2)
    
print("S= ", s)


# or: chỉ cần 1 vế đúng
# and: 2 vế đều phải đúng

# xử lý nhập điểm Toán trong khoảng từ 0 đến 10
diemToan = float(input("Nhập điểm toán = "))
while (diemToan < 0 or diemToan > 10):
    diemToan = float(input("Nhập lại điểm toán = "))
    
# xử lý nhập điểm tiếng Anh trong khoảng từ 0 đến 10    
diemTA = float(input("Nhập điểm tiếng Anh = "))
while (diemTA < 0 or diemTA > 10):
    diemTA = float(input("Nhập lại điểm Anh = "))
    
# xử lý nhập điểm tiếng Việt trong khoảng từ 0 đến 10    
diemTV = float(input("Nhập điểm tiếng Việt = "))
while (diemTV < 0 or diemTV > 10):
    diemTV = float(input("Nhập lại điểm tiếng Việt = "))

# tính điểm trung bình
diemTB = (diemToan*2 + diemTA + diemTV*2) / 5
# xử lý xếp loại học sinh
if (diemTB >= 8 and diemTB <=10):
    print("Xếp loại: Giỏi")
elif (diemTB >= 6.5 and diemTB < 8):
    print("Xếp loại: Khá")
elif (diemTB >= 5 and diemTB < 6.5):
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")