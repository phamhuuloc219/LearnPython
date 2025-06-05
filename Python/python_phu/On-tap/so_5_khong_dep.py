def kiem_tra_so_dep_bac_5(number):
    s = str(number)
    dem_khac_5 = 0 
    for ky_tu in s:
        if ky_tu != '5':
            dem_khac_5 += 1
        if ky_tu == '0':
            dem_khac_5 += 1
    if dem_khac_5 == 1:
        return True
    else: 
        return False
    
k = int(input("Nhap k= "))
ket_qua = []
i = 10
while len(ket_qua) < k:
    if kiem_tra_so_dep_bac_5(i):
        ket_qua.append(i)
    i += 1

print(ket_qua[-1])