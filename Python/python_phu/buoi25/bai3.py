def kiem_tra_so_chan(n):
    return n % 2 == 0

# Nhập số lượng phần tử của mảng
n = int(input("Nhập số lượng phần tử của mảng: "))
# Tạo 1 mảng rỗng
arr = []
# Nhập giá trị của từng phần tử vào mảng
for i in range(n):
    a = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(a)
    
# Sử dụng hàm để kiểm tra số chẵn trong mảng
for i in range(len(arr)):
    if kiem_tra_so_chan(arr[i]):
        print(f"Phần tử thứ {i+1} là số chẵn")
    else:
        print(f"Phần tử thứ {i+1} là số lẻ")