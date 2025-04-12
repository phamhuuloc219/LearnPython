import datetime

ngay = input("Nhập ngày sinh (Định dạng DD/mm/YYYY): ") 
ngay_sinh = datetime.datetime.strptime(ngay, "%d/%m/%Y")
# lấy ra 
hom_nay = datetime.datetime.today()

tuoi = hom_nay.year - ngay_sinh.year

if (hom_nay.month, hom_nay.day) < (ngay_sinh.month, ngay_sinh.day):
    tuoi -= 1

print("tuoi hien tai = " , tuoi)