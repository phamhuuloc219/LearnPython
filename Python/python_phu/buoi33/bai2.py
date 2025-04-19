chuoi = input("Nhập vào 1 chuỗi: ")
ki_tu = input("Nhập vào 1 ký tự: ")
dem = 0
for i in chuoi:
    if i == ki_tu:
        dem +=1
print("số lần xuất hiện của ký tự",ki_tu,"là: ", dem)