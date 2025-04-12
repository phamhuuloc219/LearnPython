import datetime
# timestamp lấy số giây đã trôi qua kể từ 00:00:00 1/1/1970
so_giay_1_ngay = 24 * 60 * 60

ngay = input("Nhập ngày (Định dạng DD/mm/YYYY): ") 
ngay_hom_nay = datetime.datetime.strptime(ngay, "%d/%m/%Y")
# lấy ra ngày hiện tại
# ngay_hien_tai = datetime.datetime.today()

# số giây kể từ 00:00:00 1/1/1970 đến ngày hiện tại
# so_giay_hien_tai = ngay_hien_tai.timestamp()
so_giay_hien_tai = ngay_hom_nay.timestamp()

so_giay_ngay_mai = so_giay_hien_tai + so_giay_1_ngay

ngay_mai = datetime.datetime.fromtimestamp(so_giay_ngay_mai)

print("Hôm nay là:", ngay_hom_nay.strftime("%d/%m/%Y"))
print("Ngày mai là:", ngay_mai.strftime("%d/%m/%Y"))