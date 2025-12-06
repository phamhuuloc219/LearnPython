# 3. Viết hàm kiểm tra số nguyên tố
# Gợi ý: Vòng lặp for, kiểm tra nếu n chia từ 1 đến n

# 6. Viết hàm đếm số ký tự nguyên âm trong chuỗi 
# def dem_nguyen_am(chuoi):
#     nguyen_am="aeiou" # tạo 1 chuỗi chứa các nguyên âm
#     dem = 0 # khởi tạo biến đếm
#     chuoi_lower = chuoi.lower() # chuyển chuỗi về chữ thường để dễ so sánh
#     for ky_tu in chuoi_lower: # lặp qua từng ký tự trong chuỗi
#         if ky_tu in nguyen_am: # kiểm tra ký tự có phải nguyên âm không
#             dem += 1 # tăng biến đếm lên 1
#     return dem

# string_test = input("Nhập chuỗi: ")
# print("Số nguyên âm trong chuỗi là:", dem_nguyen_am(string_test))
    
    
    
# 7. Viết hàm chuẩn hóa họ tên (viết hoa chữ cái đầu)
def chuan_hoa_ten(ten):
    ket_qua = ""
    name = ten.strip()  # Loại bỏ khoảng trắng thừa ở đầu và cuối
    danh_sach_name = name.split()  # Tách tên thành danh sách các từ
    
    for tu in danh_sach_name: # Lặp qua từng từ trong danh sách
        # Viết hoa chữ cái đầu và viết thường các chữ cái còn lại
        tu_chuan_hoa = tu[0].upper() + tu[1:].lower()
        
        ket_qua = ket_qua + tu_chuan_hoa + " "
    
    return ket_qua.strip()
       
s = input("Nhập họ tên: ")
print("Tên chuẩn hóa:", chuan_hoa_ten(s))
# 8. Viết hàm đảo ngược chuỗi. Không dùng cú pháp [::-1].
