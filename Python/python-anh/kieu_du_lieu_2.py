# # Kiểu danh sách (List)
# danh_sach = [321, 54.321, "abc", True, [1,2,3]]
# # Phần tử trong danh sách chấp nhận mọi kiểu dữ 
# # liệu trong python

# # Truy cập phần tử trong danh sách
# fruits = ["apple", "banana", "cherry","mango","orange" ]
# print(fruits[0]) # lấy phần tử đầu tiên 
# print(fruits[1]) # lấy phần tử thứ 2
# print(fruits[1:4]) # lấy phần tử thứ 2,3,4

# print("Danh sách trước khi thay đổi")
# print(fruits)
# fruits[1] = "blueberry" # thay đổi banana thành blueberry
# print("Danh sách sau khi thay đổi")
# print(fruits)


# # Tạo 1 danh sách trên 5 phần tử
# danh_sach = [312, 54.2, "abc", True, [1,2,3], "python"]
# # - Truy cập phần tử đầu tiên trong danh sách
# print(danh_sach[0])
# # - truy cập phần tử cuối cùng trong danh sách
# print(danh_sach[-1])
# # - Truy cập từ phần tử thứ 2 đến phần tử thứ 5
# print(danh_sach[1:5])
# # - Thay đổi phần tử thứ 3 thành "Hello"
# danh_sach[2] = "hello"
# print(danh_sach)

# danh_sach.append("senko")
# print(danh_sach)




dict = {key1 : value1, key2 :value2 ,...}
* key không được trùng nhau, value trùng thoải mái
* key ưu tiên ở kiểu dữ liệu chuỗi "key" , 'key'

# gender: true = nam , false = nữ
student = { 
           "name" : "Loc", 
           "age" : 23, 
           "gender" : True,
           "height" : 1.7
           }
# truy cập xem giá trị của từ điển
print(student["name"])
print(student["age"])
print(student["gender"])
print(student["height"])
# thay đổi giá trị của từ điển
student["height"] = 1.8
print(student["height"])

student.items() # "name" : "loc" , "age" : 23, "gender" : True, "height" : 1.7