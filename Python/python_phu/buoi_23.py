# Viết chương trình nhập một chuỗi và in ra chuỗi đảo ngược.
# python => nohtyp

chuoi = input("Nhập chuỗi: ")
chuoi_dao_nguoc = ""

for i in chuoi:
    chuoi_dao_nguoc = i + chuoi_dao_nguoc
    
# print("Chuỗi sau khi đảo ngược:", chuoi_dao_nguoc)
if chuoi == chuoi_dao_nguoc:
    ...
else:
    ...
    
    
# Phần tử
my_list = ["apple", "orange", 4.5, 6, 8.5, True, False, [3,6,2,5,5]]
# Truy xuất phần tử đầu tiên
print(my_list[0])
# Truy xuất phần tử cuối cùng
print(my_list[-1])
# Kiểm tra phần tử có trong danh sách
print("orange" in my_list)
# Nối 2 danh sách
list1 = [4,6,2,6,7,3]
list2 = ['orange1', 'orange2',True]
new_list = list1 + list2
print(new_list)




list1 = [3,1,2,3,4,3,5]
# Thêm 1 phần tử vào cuối danh sách append()
list1.append(1111)
print(list1)

# Thêm phần tử vào vị trí bất kỳ trong danh sách
# insert(vị trí, giá trị)
# Thêm phần tử apple vào vị trí thứ 4
list1.insert(3,"apple")
print(list1)


# Xóa 1 phần tử đầu tiên có giá trị trùng
# với giá trị được truyển vào trong danh sách
list1.remove(3)
print(list1)

# Xóa phần tử theo chỉ số(index): pop()
# pop(index)
# Mặc định nếu không truyền index vào
# thì giá trị bị xóa là gía trị cuối cùng
list1.pop()
# xóa phần tử thứ 4
list1.pop(3)
print(list1)



# Cho 1 danh sách [64,32,64,71]
# a. Xóa phần tử 64
# b. Thêm phần tử 14 vào cuối danh sách
# c. thêm phần tử 62 vào vị trí thứ 3 trong danh sách
# d. Xóa phần tử tại vị trí thứ nhất
# e. Cho danh sách ["apple", "orange"] ghép 2 danh sách lại với nhau