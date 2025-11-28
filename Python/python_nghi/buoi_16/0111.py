# #Khai báo hàm
# def cat_trai_cay():
#     print("Tôi là Nghi")
#     print("Đang cắt trái cây...")

# def cat_xong(fruit):
#     print(f"Đã cắt xong trái {fruit}!")

# # # Sử dụng hàm
# # trai_cay = input("Nhập tên trái cây bạn muốn cắt: ")
# # cat_trai_cay()
# # cat_xong(trai_cay)   

def tinh_tong(a, b,c):
    return a+b+c

tong = tinh_tong(5, 10, 15)

print(tong)


# def tinh_thuong(a, b):
#     if b == 0:
#         return "Lỗi: Không thể chia cho 0"
#     else:
#         return a / b

# thuong = tinh_thuong(10, 0)
# print(thuong)


# list_so = [12, 22, 13, 24, 25]

# so_lon_nhat = max(list_so)
# so_nho_nhat = min(list_so)

# print("Số lớn nhất trong list là:", so_lon_nhat)
# print("Số nhỏ nhất trong list là:", so_nho_nhat)

# pi = 3.141592653589793238462643383279

# print(round(pi, 3))

# list_so = [12, 22, 13, 24, 25, 5, 7, 9, 11, 30]

# danh_sach_sap_xep_tang_dan = sorted(list_so)
# danh_sach_sap_xep_giam_dan = sorted(list_so, reverse=True)

# print("Danh sách sau khi sắp xếp tăng dần:", danh_sach_sap_xep_tang_dan)
# print("Danh sách sau khi sắp xếp giảm dần:", danh_sach_sap_xep_giam_dan)






# def tinh_trung_binh_cong(danh_sach):
#     ket_qua = sum(danh_sach) / len(danh_sach)
#     return ket_qua

# # câu 3
# so = [12, 22, 13, 24, 25, 5, 7, 9, 11, 30]
# trung_binh_cong = tinh_trung_binh_cong(so)


# def tinh_bmi(can_nang, chieu_cao):
#     bmi = can_nang / ( chieu_cao ** 2 )
#     if bmi < 18.5:
#         return "Gầy"
#     elif bmi < 25:
#         return "Bình thường"
#     elif bmi < 30:
#         return "thừa cân"
#     else:
#         return "trà bông"


# can_nang = float(input("Nhập cân nặng: "))
# chieu_cao = float(input("Nhập chiều cao: "))

# print("BMI của tôi là: ", tinh_bmi(can_nang, chieu_cao)) # sử dụng hàm tinh_bmi




bai_tap =""" 
                        20 phút
                        
2. Viết hàm tìm số lớn nhất trong 3 số (dùng cấu trúc if-elif-else)
input : 30, 42, 31
output: 42

5. Viết hàm xếp loại tuổi (dùng cấu trúc if-elif-else)
Input: tuổi
Output: trẻ em, thiếu niên, thanh niên, trung niên, người già.

"""

def so_lon_nhat(a,b,c):
    max_number = c
    
    if(max_number < b):
        max_number = b
        
    if(max_number < a):
        max_number = a
        
    return max_number

number_1 = float(input("Nhập số thứ nhất: "))
number_2 = float(input("Nhập số thứ hai: "))
number_3 = float(input("Nhập số thứ ba: "))

print("Số lớn nhất trong ba số là:", so_lon_nhat(number_1,number_2,number_3))


# def phan_loai_tuoi(tuoi_cua_ban): 
#     if tuoi_cua_ban>=0 and tuoi_cua_ban < 12:
#         return "trẻ con"
#     elif  tuoi_cua_ban>=12 and tuoi_cua_ban < 18:
#         return "trẻ vị thành niên"
#     elif tuoi_cua_ban >= 18 and tuoi_cua_ban < 40:
#         return "trưởng thành"
#     elif tuoi_cua_ban >= 40 and tuoi_cua_ban < 65:
#         return "trung niên"
#     elif tuoi_cua_ban >= 65:
#         return "già"
#     else:
#         return "Không biết"
    
# tuoi_cua_ban = float(input("nhập tuổi của bạn: "))
# while tuoi_cua_ban < 0:
#     tuoi_cua_ban = float(input("Nhập lại tuổi của bạn: "))
# print("bạn đang nằm trong độ tuổi là: ",phan_loai_tuoi(tuoi_cua_ban))


"a,e,i,o,u"