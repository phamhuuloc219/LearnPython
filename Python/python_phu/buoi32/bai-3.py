gio_lam = float(input("Nhập số giờ làm: "))
# Nếu giờ làm < 0 thì yêu cầu người dùng nhập lại
while gio_lam < 0:
    gio_lam = float(input("Giờ làm không thể nhỏ hơn 0. Vui lòng nhập lại: "))
tien_moi_gio = float(input("Nhập số tiền môi giờ: "))
# Nếu số tiền mỗi giờ < 0 thì yêu cầu người dùng nhập lại
while tien_moi_gio < 0:
    tien_moi_gio = float(input("Tiền mỗi giờ không thể nhỏ hơn 0. Vui nhập lại: "))

gio_tieu_chuan = 44
if gio_lam >= gio_tieu_chuan:
    tien_tang_ca = tien_moi_gio*1.5
    
tien_luong = 0

if gio_lam < gio_tieu_chuan or gio_lam == gio_tieu_chuan:
    tien_luong = gio_lam * tien_moi_gio
elif gio_lam > gio_tieu_chuan:
    tien_luong = gio_tieu_chuan * tien_moi_gio + (gio_lam - gio_tieu_chuan) * tien_tang_ca
    
print("Tien luong: ", tien_luong)