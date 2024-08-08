# Cú pháp thiết lập hàm không trả lại giá trị:
# def < tên hàm > ( < tham số > ):
#     <khối lệnh >
#     return
# Chú thích: Lệnh return không có giá trị trả lại. Hàm kết thúc khi gặp lệnh return .
# Nếu hàm không trả lại giá trị thì có thể không cần lệnh return

# =>  Để thiết lập hàm trả lại gia trị, câu lệnh return trong khai báo hàm
# cần có <giá trị> đi kèm. Để thiết lập hàm không trả lại giái trị có thể
# dùng lênh return không có  <giá trị> hoặc không cần có return.

# chuoi_goc = str(input("nhap chuoi goc: "))
# ky_tu = str(input("nhap ky tu: "))
# dem = 0
# for i in chuoi_goc:
#         if i in ky_tu:
#             dem+=1
# print(dem)

# def dao_nguoc(string):
#     chuoi_dao_nguoc = ""
#     for character in string:
#         chuoi_dao_nguoc = character + chuoi_dao_nguoc
#     return chuoi_dao_nguoc

# string = "đây là một chuỗi ví dụ"
# chuoi_dao_nguoc = dao_nguoc(string)
# print(chuoi_dao_nguoc)

# chuoi_goc = str(input("nhap chuoi goc: "))
# word_count = chuoi_goc.split()
# print(word_count)
# max = word_count[0]
# for i in word_count:
#     if word_count[i] > max:
#         max = word_count[i]
# print(max)

# Bài 1. Viết chương trình nhập vào một mảng số nguyên gồm n phần tử. Tìm và in ra màn hình phần tử lớn nhất chia hết cho 3 có trong mảng
# def so_lon_nhat_chia_het_cho_3():
#     # Duyệt mảng
#     n = int(input("Nhập vào số phần tử của mảng: "))
#     mang = []
#     for i in range(n):
#         mang.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
#     # Tìm số lớn nhất chia hết cho 3
#     max = 0
#     for i in range (len(mang)):
#         if mang[i] > max and mang[i]%3==0:
#             max = mang[i]
#             print("Phần tử lớn nhất chia hết cho 3 là: ",max)
#         else:
#             print("Không có phần tử nào chia hết cho 3.")
# so_lon_nhat_chia_het_cho_3()

# Bài 2. Viết chương trình nhập vào một mảng số nguyên gồm n phần tử.
# a. Tìm và in ra màn hình các số lẻ có trong mảng
# b. Tìm và in ra màn hình số lớn nhất và số nhỏ nhất có trong mảng

# def so_le(mang):
#     print("Các số lẻ có trong mảng: ")
#     for i in range (len(mang)):
#         if mang[i] % 2 != 0:
#             print(mang[i])
            
# n = int(input("Nhập vào số phần tử của mảng: "))
# mang = []
# for i in range(n):
#     mang.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
# so_le(mang)

# def phan_loai_hs(score):
#     if not (0 <= score <= 100):
#         return "Điểm không hợp lệ"
    
#     match score:
#         case score if score >= 90:
#             return "Xuất sắc"
#         case score if score >= 80:
#             return "Giỏi"
#         case score if score >= 70:
#             return "Khá"
#         case score if score >= 60:
#             return "Trung bình"
#         case _:
#             return "Yếu"
# score = int(input("Nhập điểm: "))
# print(phan_loai_hs(score))