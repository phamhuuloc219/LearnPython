# Nhập số lượng phần tử của mảng
n = int(input("Nhập số lượng phần tử của mảng: "))
# Tạo 1 mảng rỗng
arr = []
# Nhập giá trị của từng phần tử vào mảng
for i in range(n):
    a = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(a)
# Khởi tạo biến tong
tong = 0
# Tính tổng các phần tử chia hết cho 7
for i in range(len(arr)):
    if arr[i] % 7 == 0:
        tong += arr[i]
print("Tổng các phần tử chia hết cho 7 là: ",tong)
