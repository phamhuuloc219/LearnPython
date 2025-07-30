# gio = int(input("Nhập giờ: "))

# if (gio >= 5 and gio <= 11):
#     print("Buổi sáng")
# elif (gio >= 12 and gio <= 17):
#     print("Buổi chiều")
# elif (gio >= 18 and gio <= 22):
#     print("Buổi tối")
# elif (gio == 23 or (gio >= 0 and gio <= 4)):
#     print("Buổi khuya")
# else:
#     print("Giờ không hợp lệ")

tong_diem = 0
toan = float(input("Nhập điểm Toán: "))
anh = float(input("Nhập điểm Anh: "))
van = float(input("Nhập điểm Văn: "))

tong_diem = (toan + anh + van)/3

if (tong_diem >= 8 and tong_diem <=10):
    print("Xếp loại: Giỏi")
elif (tong_diem >= 6.5 and tong_diem <8):
    print("Xếp loại: Khá")
elif (tong_diem >= 5 and tong_diem < 6.5):
    print("Xếp loại: Trung bình")
elif (tong_diem >= 3.5 and tong_diem < 5):
    print("Xếp loại: Yếu")
elif (tong_diem >= 0 and tong_diem < 3.5):
    print("Xếp loại: Cá Biệt")
else: 
    print("Điểm không hợp lệ")