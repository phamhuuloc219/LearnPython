# Viết chương trình yêu cầu người dùng nhập một số nguyên dương.
# Nếu nhập sai thì yêu cầu nhập lại cho đến khi đúng và in ra thông báo.

# while <Điều kiện lặp>:
#     <Lệnh lặp>

n = int(input("Nhập n = "))
while n <= 0:
    print("Số nhập phải lớn hơn 0")
    n = int(input("Nhập n = "))
print("Số bạn vừa nhập là ", n,"dfsdfs")

# Viết chương trình yêu cầu người dùng nhập một số nguyên dương n. Kiểm tra trong
# khoảng từ 1 đến n có bao nhiêu số chẵn và lẻ sau đó in ra màn hình tổng số chẵn 
# và lẻ trong khoảng từ 1 đến n

n = int(input("Nhập n = "))
while n <= 0:
    print("Số nhập phải lớn hơn 0")
    n = int(input("Nhập n = "))

dem_chan = 0
dem_le = 0
for i in range (1, n+1):
    if i % 2 == 0:
        dem_chan += 1
    else:
        dem_le += 1
print(f"Trong khoang tu 1 den {n} co {dem_chan} so chan va {dem_le} so le")

# Viết một chương trình Python để phân loại học sinh theo điểm thi
# trung bình cộng 3 môn Toán-Lý-Hóa, với Toán là môn nhân hệ số 2. 
# Điều kiện là chương trình sẽ nhập 3 điểm thi của học sinh (số thực từ 0 đến 10)
# và in ra xếp loại tương ứng dựa trên thang điểm sau: 
# Giỏi: 8.0 - 10.0
# Khá: trên 6.5 đến dưới 8.0
# Trung bình: trên 4.5 đến dưới 6.5 
# Yếu: từ 0 đến dưới 4.5

diem_toan = float(input("Nhập điểm toán: "))
while diem_toan < 0 or diem_toan > 10:
    print("Điểm toán phải nằm trong khoảng 0-10")
    diem_toan = float(input("Nhập điểm toán: "))
###################################################    
diem_ly = float(input("Nhập điểm lý: "))
while diem_ly < 0 or diem_ly > 10:
    print("Điểm lý phải nằm trong khoảng 0-10")
    diem_ly = float(input("Nhập điểm lý: "))
###################################################
diem_hoa = float(input("Nhập điểm hóa: ")) 
while diem_hoa < 0 or diem_hoa > 10:
    print("Điểm hóa phải nằm trong khoảng 0-10")
    diem_hoa = float(input("Nhập điểm hóa: "))

# Tính điểm trung bình
diem_trung_binh = (diem_toan*2 + diem_ly + diem_hoa) / 4

# Xếp loại
if diem_trung_binh >= 8 and diem_trung_binh <= 10:
    print("Xếp loại: Giỏi")
elif diem_trung_binh >= 6.5 and diem_trung_binh < 8:
    print("Xếp loại: Khá")
elif diem_trung_binh >= 5 and diem_trung_binh < 6.5:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")