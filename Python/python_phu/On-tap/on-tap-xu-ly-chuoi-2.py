# 1. Chuẩn hóa tên người dùng
# Nhập vào họ tên viết lung tung (có thể viết hoa/lộn xộn), chuẩn hóa lại cho đúng.
# Ví dụ: "nGUyen vAn tEo" → "Nguyen Van Teo"

# str = input("Nhap ten nguoi dung: ")
# result = ""
# new_str = str.split(" ") # tách chuỗi thành danh sách
# # => new_str = ['nguyEn', 'dInH', 'XUan', 'PhU']
# # duyệt qua từng phần tử trong danh sách new_str
# for i in new_str: 
#     result = result + i.capitalize() + " "
# print(result)

# def chuan_hoa_ten(str):
#     result = ""
#     new_str = str.split(" ") # tách chuỗi thành danh sách
#     # => new_str = ['nguyEn', 'dInH', 'XUan', 'PhU']
#     # duyệt qua từng phần tử trong danh sách new_str
#     for i in new_str: 
#         result = result + i.capitalize() + " "
    
#     return result

# str = input("Nhap ten nguoi dung: ").strip()
# print(str)
# print(chuan_hoa_ten(str))

# 2. Tìm từ dài nhất
# Nhập một câu. In ra từ dài nhất trong câu.
# string = input("Nhap mot cau: ").strip() # strip() loại bỏ khoảng trắng ở 2 đầu chuỗi kí tự
# new_string = string.split(" ")
# tu_dai_nhat = new_string[0]

# for i in new_string:
#     if len(i) > len(tu_dai_nhat):
#         tu_dai_nhat = i
# print("Từ dài nhất trong câu là: ",tu_dai_nhat)

# 3. Tìm số lượng kí tự a, e, o, u, i trong chuỗi được nhập từ bàn phím.
# Ví dụ:  nhập vào chuỗi: "xin chao cac ban"
# Kết quả python in ra
# - số lượng kí tự a: 3
# - số lượng kí tự e: 0
# - số lượng kí tự o: 1
# - số lượng kí tự u: 0
# - số lượng kí tự i: 1

# 

# Duyệt qua từng kí tự trong chuoi => for
# Kiểm tra kí tự đó có phải là 'a', 'e', 'o', 'u', 'i' hay không => if-elif-else
# Nếu bằng thì => tăng biến đếm của kí tự bằng đó lên
# in ra màn hình kết quả

# dem_a = dem_e = dem_o = dem_u = dem_i = 0
# chuoi = input("Nhập một chuỗi: ").strip()  
# for ky_tu in chuoi.lower():  
#     if ky_tu == 'a':
#         dem_a += 1
#     elif ky_tu == 'e':
#         dem_e += 1
#     elif ky_tu == 'o':
#         dem_o += 1
#     elif ky_tu == 'u':
#         dem_u += 1
#     elif ky_tu == 'i':
#         dem_i += 1

# print(f"Số chữ a: {dem_a}")
# print(f"Số chữ e: {dem_e}")
# print(f"Số chữ o: {dem_o}")
# print(f"Số chữ u: {dem_u}")
# print(f"Số chữ i: {dem_i}")

danh_sach_ki_tu = ['a', 'e', 'o', 'u', 'i']
chuoi = input("Nhập một chuỗi: ").strip().lower()

for ky_tu in danh_sach_ki_tu:
    dem = 0
    for i in chuoi:
        if i == ky_tu:
            dem += 1
    print(f"Số chữ {ky_tu}: {dem}")
    