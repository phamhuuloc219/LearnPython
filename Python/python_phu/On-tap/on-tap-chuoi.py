#5. Viết chương trình yêu cầu người dùng nhập một chuỗi và in ra độ dài của chuỗi đó.
#6. Nhập một chuỗi và một ký tự, đếm số lần ký tự đó xuất hiện trong chuỗi.
#7. Viết chương trình nhập một chuỗi và in ra chuỗi đảo ngược.
# 8. Viết chương trình nhập một chuỗi và kiểm tra xem nó có phải là chuỗi đối xứng không (ví dụ: "madam", "radar").
# 7. Cách 1
a = "xin chào các bạn hôm nay tôi học python"
print(a[::-1])
# Cách 2
s = input("Nhập chuỗi: ")
chuoi_dao_nguoc = ""

for i in s:
    chuoi_dao_nguoc = i + chuoi_dao_nguoc
print(chuoi_dao_nguoc)

# 6. Cách 1
s = input("Nhập chuỗi: ")
ky_tu = input("Nhập ký tự cần đếm: ")

print("Ký tự",ky_tu," xuất hiện:",s.lower().count(ky_tu))

# Cách 2
s = input("Nhập chuỗi: ")
ky_tu = input("Nhập ký tự cần đếm: ")
dem = 0
for i in s:
    if i == ky_tu:
        dem = dem + 1
print("Ký tự",ky_tu," xuất hiện:",dem)


# 8
s = input("Nhập chuỗi: ")
chuoi_dao_nguoc = ""

for i in s:
    chuoi_dao_nguoc = i + chuoi_dao_nguoc
    
if s == chuoi_dao_nguoc:
    print("Chuỗi",s,"là chuỗi đối xứng")
else:
    print("Chuỗi",s,"không phải là chuỗi đối xứng")