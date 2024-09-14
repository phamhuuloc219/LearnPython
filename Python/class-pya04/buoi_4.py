# """
# 1. Viết chương trình nhận hai số từ người dùng và tính tổng, hiệu, tích, thương của chúng.

# 2.  Viết chương trình nhận một số nguyên từ người dùng và tính bình phương và lập phương của số đó.

# 3. Viết chương trình nhận hai số nguyên x, y, sau đó tính: p=x*y, s=x+y, total=s+p(s-x)*(p+y) và in kết quả.

# 4. Viết chương trình nhập điểm kiểm tra (30%), điểm thi giữa kỳ(30%), điểm thi cuối kỳ (40%) 
# và tính tổng điểm, sau đó in kết quả.

# # 5. Viết chương trình tính diện tính hình tròn, vuông, tam giác, chữ nhật.

# 6. Viết chương trình nhập vào 1 số và kiểm tra số chẵn hay lẻ.

# 7. Viết chương trình nhập vào 2 số . Kiểm tra và so sánh sau đó in ra màn hình số lớn nhất
# """

# num = int(input("Nhập một số nguyên: "))
# nhi_phan = bin(num)
# print(f"Số {num} dưới dạng nhị phân là: {nhi_phan[2:]}")


year = int(input("Nhập năm: "))
if (year % 4 ==0 and year % 100 != 0) or (year % 400 ==0):
    print("Năm nhuận")
else:
    print("Không phải năm nhuận")