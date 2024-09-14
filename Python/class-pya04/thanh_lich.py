#Bài tập
# #3
# x = float(input("nhập điểm kiểm tra: "))
# y = float(input("Nhập điểm giũa kì: "))
# z = float(input ("Nhập điểm cuối kì: "))
# diem_tong = ((x*20) + (y*30) + (z*50))/100
# if (diem_tong >= 9.0 and diem_tong<10):
#     print("hạng A")
# elif (diem_tong <9.0 and diem_tong >= 7.0):
#     print("hạng B")
# elif (diem_tong <7.0 and diem_tong >= 5.0):
#     print("hạng C")
# elif (diem_tong <5.0 and diem_tong >0):
#     print("Hạng D")
#5
# tien = int(input("Nhập số tiền bạn kiếm được:"))
# if (tien > 0 and tien <= 100):
#     hoa_hong = (tien*5)/100
# elif (tien > 100 and tien <= 300):
#     hoa_hong = (tien*10)/100
# elif (tien > 300 ):
#     hoa_hong = (tien*20)/100
# print(hoa_hong)
# #6
# phi_thue_bao = 25000
# phut_goi = int(input("Nhập số phút gọi: "))
# if (phut_goi > 0 and phut_goi <50):
#     so_tien = phi_thue_bao
# elif ( phut_goi >=50 and phut_goi <150):
#     so_tien = phi_thue_bao + (500*phut_goi)
# elif ( phut_goi >=150 and phut_goi <200):
#     so_tien = phi_thue_bao + (400*phut_goi)
# elif ( phut_goi >200):
#     so_tien = phi_thue_bao + (200*phut_goi)
# print (so_tien)
#7
#7
tien_luong = int(input("Nhập tiền lương: "))
if (tien_luong == 15):
    tru_thue = tien_luong-(tien_luong*(30/100))
elif (tien_luong >= 7 and tien_luong<15):
    tru_thue = tien_luong-(tien_luong*(20/100))
elif (tien_luong >0 and tien_luong<7):
    tru_thue = tien_luong-(tien_luong*(10/100))
print(tru_thue)