#Từ điển (dictionary): Kiểu dữ liệu từ điển chứa các cặp khóa-giá trị, trong đó mỗi khóa phải là duy nhất và không thay đổi, và được đặt trong dấu ngoặc nhọn {}.
# student={"Ten: Loc","Tuoi:21","Lop:63cntt-1"}

################################################################
#Danh sach []
# list=[1,2,3,4,5,6,7,8,9,10]
# print(student)
# print(list[2])

################################################################
#Tập hợp (set): Kiểu dữ liệu tập hợp chứa một tập hợp các phần tử duy nhất và không có thứ tự, và được đặt trong dấu ngoặc nhọn {}.
# primes={2,3,5,7,11}

################################################################
#Bộ (tuple): Kiểu dữ liệu bộ chứa một tập hợp các phần tử không thay đổi, và được đặt trong dấu ngoặc đơn ().
# point=(10,20)
################################################################
# Bai tap
a=input("Nhap nam sinh cua ban: ")
b=2024
c=int(b) - int(a)
print("Tuoi hien tai cua ban la:" + str(c));
if c<22:
    print(str(c)+ " "+"Là sắp già rồi")
else:
    print(str(c)+" " +"Là già rồi ")