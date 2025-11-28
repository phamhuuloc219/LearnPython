n = int(input("Nhập số phần tử: "))

danh_sach = []
tong = 0

for i in range(n):
    so = int(input(f"Nhập giá trị phần tử thứ {i + 1}: "))
    danh_sach.append(so)

for i in range(len(danh_sach)):
    if danh_sach[i] % 7 == 0:
	    tong += danh_sach[i]
print("Tổng các số chia hết cho 7:", tong)
