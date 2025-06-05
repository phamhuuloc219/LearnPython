k = int(input("Nhap k= "))
day_thang = "" #123456789101112123456789101112....
for i in range(1, 13):
    day_thang += str(i)

tong = 0
dem = 0
i = 0
while dem < k:
    chi_so = i % len(day_thang)
    so = int(day_thang[chi_so])
    tong += so
    dem +=1
    i +=1
print("Tổng",k,"chữ số đầu tiên là: ",tong)