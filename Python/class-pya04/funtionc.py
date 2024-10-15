# # # def xin_chao():
# # #     print("Chào mừng bạn đến với chương trình Python!")

# # # xin_chao()

# # def tinh_tong():
# #     num1 = float(input("Nhập số thứ nhất: "))
# #     num2 = float(input("Nhập số thứ hai: "))
# #     tong = num1 + num2
# #     print(f"Tong của {num1+num2} và {num2} là: {tong}")
# #     print("Tong cua",num1 + num2,"va",num2,"la:",tong)
    
# # # tinh_tong()

# # def add(a,b):
# #     tong = a + b
# #     hieu = a - b
# #     return tong
# # def thuong(a,b):
# #     global x
# #     c =0 
# #     while b == 0:
# #         print("Số b phải khác 0!")
# #         b = int(input("b = "))
# #     return a/b
# # x = int(input("x= "))
# # y = int(input("y= "))
# # print(add(x,y))
# # print(thuong(x,y))

# # #Viết hàm yêu cầu người dùng nhập họ tên
# # # rồi đưa lời chào ra màn hình
# def hello(name):
#     return "hello " + name
# name = input("nhap ho ten: ")
# print(hello(name))
# # #Viết hàm tìm số lớn nhất của hai số nguyên dương được người dùng
# # # nhập từ bàn phím rồi in kết quả ra màn hình
# def sln(a,b):
#     if a > b:
#         return a
#     elif a == b:
#         return "Hai so bang nhau"  # or return "Số bang nhau" for Python 3.x compatibility
#     else:
#         return b
# x = int(input("x= "))
# y = int(input("y= "))
# print("so lon nhat trong hai so la: ",sln(6,7))
# def arr():
#   list = int(input("Nhập số lượng phần tử của danh sách:" ))
#   my_list = []
#   for i in range(list):
#     n = input(f"Nhap so thu {i + 1}: ")
#     my_list.append(n)
#   print("Danh sách vừa nhập: ", my_list)
# arr()
# a = [7,3,5,1,2,4,9,6]
# print(sorted(a, reverse=True))
# a.insert(3,19)
# print(a)
def tim_chuoi_co_do_dai(strings, do_dai):
    ket_qua = []
    for chuoi in strings:
        if len(chuoi) == do_dai:
            ket_qua.append(chuoi)
    return ket_qua

danh_sach_chuoi = input("Nhập danh sách chuỗi, cách nhau bằng dấu phẩy: ").split(',')

do_dai_can_tim = int(input("Nhập độ dài cần tìm: "))

ket_qua = tim_chuoi_co_do_dai(danh_sach_chuoi, do_dai_can_tim)

print(ket_qua)