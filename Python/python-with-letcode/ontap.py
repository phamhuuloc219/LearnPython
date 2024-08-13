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


# 1. Viết chương trình Python để thực hiện các yêu cầu sau: 
# - Tạo một danh sách chứa tên và giá của các loại trái cây có trong một cửa hàng (trên 5 loại trái cây khác nhau). 
# [{"name": "Táo", "price": 1000}, {"name": "Chuối  ", "price": 1200}, ...]

# - In ra bảng giá trái cây của cửa hàng này theo thứ tụ bản chữ cái.
# Chuối: 1200đ
# Táo: 1000đ
# ...

# - Hỏi người dùng nhập một loại trái cây và số lượng muốn mua. 
# Hãy nhập tên trái cây:
# Hãy nhập số lượng trái cây:

# - Kiểm tra xem loại trái cây người dùng nhập có trong Danh Sách hay không. 
# + Nếu có, in ra thông báo 
# "Bạn đã mua [số lượng trái cây] [tên trái cây] với tổng số tiền: [tổng số tiền mua trái cây]". 
# + Nếu không, in ra thông báo 
# "Loại trái cây [tên trái cây] không có trong cửa hàng!"

fruits=[
    {"Name": "táo", "price": 1000},
    {"Name": "chuối", "price": 1500},
    {"Name": "cam", "price": 1200},
    {"Name": "xoài", "price": 1800},
    {"Name": "bưởi", "price": 2100}
]
def bubble_sort(fruits):
    n=len(fruits)
    for i in range(n):
        for j in range(0, n-i-1):
            if fruits[j]["price"]<fruits[j+1]["price"]:
                fruits[j], fruits[j+1]=fruits[j+1], fruits[j]
                return fruits
            bubble_sort(fruits)
            print(f"Bảng giá trái cây: ")

def sort_alphaB():
    for i in range(len(fruits)-1):
        for j in range( i+1 , len(fruits)): # 1->5
            if fruits[i]["Name"] > fruits[j]["Name"]:
                fruits[i], fruits[j] = fruits[j], fruits[i]
                # fruits[i] = fruits[j]
                # fruits[j] = fruits[i]
# lan 1: i = 0
#   j = 1
#   fruits[0]["tao"] > fruits[1]["chuoi"] => chuoi, Tao,....
#   j = 2
#   fruits[0] > fruits[2]
#   fruits[0]["chuoi"] > fruits[2]["cam"]


for fruit in fruits:
    print(f"{fruit["Name"]}: {fruit["price"]} đ")
fruit_name=input("Nhập tên trái cây: ")
quantity=int(input("Nhập số lượng trái cây: "))
found=False
total_price=0
for fruit in fruits:
    if fruit["Name"]==fruit_name:
        found=True
        total_price=fruit["price"]*quantity
        break
if found:
    print(f"Bạn đã mua {quantity} trái {fruit_name} với tổng số tiền: {total_price} đ")
if not found:
    print(f"Loại trái cây: {fruit_name} không có trong cửa hàng")