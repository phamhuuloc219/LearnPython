# # List: có thể chứa nhiều kiểu dữ liệu khác nhau
# # ví dụ: int, float, str, bool, list
# fruits = ["mango","apple", "banana"]
# # lấy ra phần tử đầu tiên của danh sách
# print(fruits[0])
# # lấy ra phần tử thứ ba của danh sách
# print(fruits[2])
# # Cách 1
# # lấy ra phần tử cuối cùng của danh sách
# print(fruits[3])
# # Cách 2
# # Lấy ra phần tử cuối cùng của danh sách
# # => lấy ra chỉ số = -1
# print(fruits[-1])

# fruits = ["mango","apple", "banana"]
# print(fruits)
# # Thay đổi apple thành cherry
# fruits[1] = "cherry"
# print(fruits)
# # thay đổi phàn tử cuối cùng
# fruits[-1] = 100
# print(fruits)

"""



"""
# # append(item): Thêm một phần tử vào cuối danh sách.
fruits = ["mango","apple", "cherry","tomato","banana"]
print(fruits)

# pop(index): Xóa phần tử tại chỉ số index và trả về giá trị của nó
fruits.pop(2)
print(fruits)

# fruits.append("strawberry")
# print(fruits)

# # remove(item): Xóa phần tử đầu tiên có giá trị là item.
# fruits.remove("apple")
# print(fruits)




# dictionary: từ điển chứa cặp Key : Value
# key: luôn luôn là kiểu dữ liệu chuỗi (string)
# value: có thể là bất kì kiểu dữ liệu nào
# dict = {
#     "name": "Loc", 
#     "age": 21, 
#     "gender": True,
#     "height": 1.68,
#     "class" : ["Python", "JavaScript", "Scratch"]   
#     }

# print(dict)

# print("Tên là: ",dict["name"])
# print("Tuổi: ",dict["age"])
# print("Chiều cao: ",dict["height"])

# fruits = ["mango","apple", "banana"]
# print(fruits[0])