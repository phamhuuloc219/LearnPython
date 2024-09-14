# # tuổi
# a = 21
# # chiều cao
# # tính bằng mét
# b = 1.68
# # tên
# name = "Loc"
# # có phải giới tính nam hay không?
# is_male = True

# """
# Bài tập biến và kiểu dữ liệu
# tạo mỗi biến là 1 kiểu dữ liệu và in ra màn hình
# """
# print("Tuoi: ",a)
# print("Chieu cao: ",b)
# print("Ten: ",name)
# print("La nam: ",is_male)
# # list: danh sách
# # cú pháp: ten_bien = [giá trị]
# fruits = [10, 12.4, "Apple", True,4,1,1,4,3,34,3,42,34,234,4345,234,23,4,23,22,"end"]
# # fruitS = 10
# # Lấy phần tử cuối cùng cuar danh sách => truyền vào index là -1
# print(fruits[-1])

"""
Bài tập: Tạo 1 danh sách hoa quả
fruits = ["apple","banana","mango","blueberry","cherry"]
a. In ra màn hình mango
b. in ra màn hình phần tử đầu tiên
c. in ra màn hình phần tử cuối cùng
d. Đếm số phần tử có trong danh sách 
"""
# fruits = ["apple","banana","mango","blueberry","cherry"]
# fruits[2] = "hello"
# print(fruits)
# trai_cay = ("apple","cherry","mango","blueberry","cherry")
# print(trai_cay[1])

student = {
    "name": "Loc",
    "age": 21,
    "phone" : "0376282119",
    "address" : "Nha Trang",
    "school" : "NTU"
}
print("Tên trước khi đổi:")
print(student)

student["name"] = "Phong"
print("Tên sau khi đổi:")
print(student)

print("Lấy tất cả các key trong từ điển:")
print(student.keys())
print("Lấy tất cả các value trong từ điển:")
print(student.values())