# Nhập một danh sách từ bàn phím
# # Cách 1:
# arr = input("Nhập các phần tử của danh sách (Cách nhau bởi 1 khoảng trắng): ") 
# # tách chuỗi vừa nhập thành danh sách
# arr = arr.split(";")
# print(arr)

# Cách 2:
# danh_sach = []
# n = int(input("Nhập số lượng phần tử có trong danh sách: "))
# for i in range(n):
#     arr = int(input(f"Nhập phần tử thứ {i+1}: "))
#     danh_sach.append(arr)
# print(danh_sach)
    
# 1. Viết chương trình nhập vào 1 danh sách các số nguyên gồm 10 phần tử.
# In ra danh sách các số chẵn có trong danh sách

danh_sach = []
n = int(input("Nhập số lượng phần tử có trong danh sách: "))
for i in range(n):
    arr = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(arr)
# print(danh_sach)
# print("Các số chẵn có trong danh sách là: ")
tong = 0
for i in range(len(danh_sach)):
    if danh_sach[i] > 0:
        # print(danh_sach[i], end=" ")
        tong += danh_sach[i]
        
print(tong)

# 2. Viết chương trình nhập vào 1 danh sách các số nguyên gồm 10 phần tử.
# In ra danh sách các số lẻ và chia hết cho 3 có trong danh sách

# 3. Viết chương trình nhập vào 1 danh sách các số nguyên gồm 10 phần tử.
# Tính tổng các phần tử có trong danh sách

# tong = 0
# for i in range(len(danh_sach)):
#     tong += danh_sach[i]
#     tong = tong + danh_sach[i]
    
# 4. Viết chương trình cho danh sách 10 phần tử True/False bất kỳ.
# Tính số lượng giá trị True có trong danh sách.
# temp = ["True", "False", "True", "False", "True", "False", "True", "False", "True", "False"]
# dem = 0
# for i in range(len(temp)):
#     if temp[i] == "True":
#         dem += 1
# print("số lượng giá trị True có trong danh sách: ",dem)

# 5. Viết chương trình nhập vào 1 danh sách các số nguyên gồm n phần tử.
# sắp xếp danh sách theo thứ tự tăng dần và giảm dần

ds = [5,7,1,534,76,23,956,342,745]
# Sắp xếp tăng dần
ds.sort()
print("Sắp xếp theo thứ tự tăng dần: ",ds)

# Sắp xếp giảm dần
ds.sort(reverse=True)
print("Sắp xếp theo thứ tự giảm dần: ",ds)

# 6. Viết chương trình nhập vào 1 danh sách các số nguyên gồm n phần tử.
# Đếm số lượng phần tử xuất hiện nhiều nhất trong danh sách.
# Ví dụ: ["apple", "orange, "apple", "orange", "apple", "blue", "red","blue"]