n = int(input("Nhập số phần tử: "))

danh_sach = []

for i in range(n):
    so = int(input(f"Nhập giá trị phần tử thứ {i + 1}: "))
    danh_sach.append(so)

max = danh_sach[0] # Giả sử phần tử đầu tiên là lớn nhất

for phan_tu in danh_sach:
    if phan_tu > max:
        max = phan_tu
        
print("Giá trị lớn nhất trong danh sách là:", max)