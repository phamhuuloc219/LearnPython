# 1.Viết chương trình in ra bảng cửu chương từ 2-9

# vòng lặp đại diện cho bảng cưu chương 2-9
for i in range(2, 10):
    # vòng lặp đại diện cho nhân từ 1-10
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
        # print(i," x ",j," = ",i*j)
    print("==================")      
       
# 2. Nhập số nguyên dương n bất kỳ. Viết chương trình
#  vẽ tam giác "*" có chiều cao là n hàng.

# 3. Viết chương trình tính kết quả biểu thức
# S= 1+1/2^3+1/3^3+...+1/n^3 (làm tròn 5 chữ số thập phân).
# n = int(input("Nhap n= "))
# tong = 0
# for i in range(1, n+1):
#     tong = tong + 1/(i**3)
# print("Ket qua la: ", round(tong,5)) 
# hàm round dùng để làm tròn chữ số thập phân

# 4. Nhập 2 số nguyên x và y.Viết chương trình tính tổng 
# bình phương các số từ x đến y.(Bình phương = mũ 2)s