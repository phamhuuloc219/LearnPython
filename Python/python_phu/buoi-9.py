# # Bài tập 1: In các số lẻ từ 10 đến 30
# for i in range(10,31):
#     if i % 2 != 0:
#         print(i)
# # Bài tập 2: Tính tổng các số từ 2 đến 40
# tong = 0
# for i in range(2,41):
#     tong = tong + i
# print(tong)
# # Bài tập 3: In bảng cửu chương của số 7
# for i in range(1,11):
#     print(7,"x",i,"=",7*i)

# break: dừng lại vòng lặp
# for i in range(1,11):
#     if i == 5:
#         break
#     else:
#         print(i)

# continue: bỏ qua lần lặp và tiếp tục chạy cho đến hết vòng lặp
# for i in range(1,11):
#     if i == 5:
#         continue
#     else:
#         print(i)

# Bài 1: Viết chương trình nhập vào 2 số a và b.
# In ra các số từ a đến b (gồm cả a và b).
# a = int(input("Nhap so nguyen a: ")) # 5
# b = int(input("Nhap so nguyen b: ")) # 10
# for x in range(a,b+1):
#     print(x)

# Bài 2: Viết chương trình nhập vào 2 số n và m.
# In ra các số từ n đến m, nếu số đó chia hết
# cho 7 thì dừng lại chương trình. 
# n = int(input("Nhap so nguyen n: ")) # 5
# m = int(input("Nhap so nguyen m: ")) # 10
# for x in range(n,m+1):
#     if x % 7 == 0:
#         break
#     else:
#         print(x)

# Bài 3: Nhập số nguyên n. Tính giá trị biểu thức S= 1.2 + 2.3 + 3.4 + ... + n(n+1). 

# hàm range chỉ được nhận vào là các số nguyên
# range(start, stop, step)
# range(1, 5, 1) => đúng
# range(0.5 , 1.5 , 0.4) => sai



for i in range(2,10):
    for o in range(1,11):
        print(i,"x",o,"= ",i*o)