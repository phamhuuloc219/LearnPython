# phan_tu = int(input("Nhập số lượng phần tử: "))
# danh_sach = []
# tong = 0
# for i in range(1, phan_tu + 1):
#     gia_tri_phan_tu = int(input(f"Nhập phần tử thứ {i}: "))
#     danh_sach.append(gia_tri_phan_tu)
    
# for i in range(len(danh_sach)):
#     tong = tong + danh_sach[i]
# print("tổng các phần tử trong danh sách la: ", tong)

# ds = []
# n = int(input("Bạn muốn nhập bao nhiêu số? "))
# for i in range(n):
#     so = int(input(f"Nhập số thứ {i+1}: "))
#     ds.append(so)
# tong_chan = 0
# tong_le = 0
# for so in ds:
#     if so % 2 == 0:
#         tong_chan = tong_chan + so
#     else:
#         tong_le = tong_le + so
# print("Tổng các số chẵn là:", tong_chan)
# print("Tổng các số lẻ là:", tong_le)

# 1. Nhập vào 1 danh sách số nguyên, Tính tổng các phần tử trong danh sách
phan_tu = int(input("Nhập số lượng phần tử: "))
danh_sach = []

for i in range(1, phan_tu + 1):
    danh_sach.append(int(input(f"Nhập phần tử thứ {i}: ")))

tong = 0
for x in danh_sach: # cách 1
    tong += x

for i in range(len(danh_sach)): # cách 2
    tong = tong + danh_sach[i]
    
    
print("Tổng các phần tử là:", tong)

# 2. Nhập vào 1 danh sách số nguyên. Tính tổng các số lẻ và các số chẵn trong danh sách
phan_tu = int(input("Nhập số lượng phần tử: "))
danh_sach = []

for i in range(1, phan_tu + 1):
    danh_sach.append(int(input(f"Nhập phần tử thứ {i}: ")))

tong_chan = 0
tong_le = 0

for x in danh_sach:
    if x % 2 == 0:
        tong_chan += x
    else:
        tong_le += x

print("Tổng số chẵn:", tong_chan)
print("Tổng số lẻ:", tong_le)
# 3. Nhập vào 1 danh sách số nguyên. Tìm phần tủ lớn nhất trong danh sách và vị trí của nó
phan_tu = int(input("Nhập số lượng phần tử: "))
danh_sach = []
vi_tri = 0

for i in range(1, phan_tu + 1):
    gia_tri_phan_tu = int(input(f"Nhập phần tử thứ {i}: "))
    danh_sach.append(gia_tri_phan_tu)
    
so_lon_nhat = danh_sach[0] # phần tử đầu tiên

for i in range(len(danh_sach)):
    if danh_sach[i] > so_lon_nhat:
        so_lon_nhat = danh_sach[i]
        vi_tri = i + 1
print("Phần tử lớn nhất trong danh sách la: ", so_lon_nhat)
print("Vị trí cua phần tử lớn nhất trong danh sách la: ", vi_tri)
# 4. Nhập vào 1 danh sách số nguyên. Tìm phần tủ bé nhất trong danh sách
phan_tu = int(input("Nhập số lượng phần tử: "))
danh_sach = []

for i in range(1, phan_tu + 1):
    danh_sach.append(int(input(f"Nhập phần tử thứ {i}: ")))

so_nho_nhat = danh_sach[0]

for x in danh_sach:
    if x < so_nho_nhat:
        so_nho_nhat = x

print("Phần tử nhỏ nhất:", so_nho_nhat)
# 5. Nhập vào 1 danh sách số nguyên. Tính tổng các phần tử chia hết cho 3 và 5 trong danh sách
phan_tu = int(input("Nhập số lượng phần tử: "))
danh_sach = []

for i in range(1, phan_tu + 1):
    danh_sach.append(int(input(f"Nhập phần tử thứ {i}: ")))

tong = 0

for x in danh_sach:
    if x % 3 == 0 and x % 5 == 0:
        tong += x

print("Tổng chia hết cho 3 và 5:", tong)


def kiem_tra_so_chan(danh_sach):
    dem = 0
    for x in danh_sach:
        if x % 2 == 0:
            dem += 1
    return dem

n = int(input("Nhập số lượng phần tử: "))
arr = []

for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(so)

print("Số lượng số chẵn là:", kiem_tra_so_chan(arr))