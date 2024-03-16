# my_tuple=("Phạm Hữu Lộc",20,"Cam Lâm","Khánh Hòa")
# my_tuple2=tuple([6.7,7,8,6,7,7.6,8,6.9])
# my_tuple3=tuple(['Trí tuệ nhân tạo','Python'])

# ho_ten=my_tuple[0]
# tuoi=my_tuple[1]
# thanh_pho=my_tuple[2]
# tinh=my_tuple[3]

# print("Họ tên:",ho_ten)
# print("Tuổi:",str(tuoi))
# print("Thành phố:",thanh_pho)
# print("Tỉnh:",tinh)

# ten_tuoi=my_tuple[0:2]
# que_quan=my_tuple[2:4]

# print(ten_tuoi[0]+' '+str(ten_tuoi[1])+' Tuổi')
# print('Vị trí hiện tại: Thành phố '+que_quan[0]+', tỉnh ' +que_quan[1])
 
# # Sử dụng cú pháp <tên biến tuple>.count(<giá trị>)
# diemThi=my_tuple2.count(7)
# print(my_tuple[0]+" có "+str(diemThi)+" điểm là điểm 7")
# # Kết hợp 2 tuple
# mix=my_tuple+my_tuple3
# print(mix)

# # Sử dụng unpacking(giải nén) để gán giá trị từ tuple vào biến
# thong_tin=my_tuple+my_tuple3
# ten,tuoi,thanh_pho,tinh,mon_hoc_1,mon_hoc_2=thong_tin
# print(ten,tuoi,thanh_pho,tinh,mon_hoc_1,mon_hoc_2)

#####################################################################################################################################

# # Dictionary là một tập hợp các cặp key-value (khóa-giá trị), trong đó mỗi key là duy nhất và không thể thay đổi (immutable). 
# # Dictionary được đánh dấu bằng cặp ngoặc nhọn {} và các cặp key-value được phân tách bằng dấu hai chấm :.
# # Cách truy cập: ten_bien[key]

# hoc_sinh={
#     'ho_ten':'Phạm Hữu Lộc',
#     'tuoi':18,
#     'lop':'12'
# }
# # truy cập và hiển thị
# print("Họ tên:",hoc_sinh['ho_ten'])
# print("Tuổi:",hoc_sinh['tuoi'])
# print("Lớp",hoc_sinh['lop'])

# # Để thêm một phần tử vào đối tượng đã khai báo, sử dụng cấu trúc ten_bien[key] = gia_tri
# danh_sach_hoc_sinh={}
# danh_sach_hoc_sinh['hs001']={
#     'ho_ten':'Phạm Hữu Lộc',
#     'tuoi':18,
#     'lop':'12'
# }
# danh_sach_hoc_sinh['hs002']={
#     'ho_ten':'Trần Thị Mỹ Trâm',
#     'tuoi':18,
#     'lop':'12'
# }
# # print("Danh sách học sinh trước khi thay đổi:")
# # print(danh_sach_hoc_sinh['hs001'])
# # # thêm và câpj nhật phần tử
# # danh_sach_hoc_sinh['hs001']['ho_ten']='Pham Huu Loc'
# # print("Danh sách học sinh sau khi thay đổi:")
# # print(danh_sach_hoc_sinh['hs001'])

# # print("Danh sách học sinh trước khi thay đổi:")
# # print(danh_sach_hoc_sinh)
# # print(len(danh_sach_hoc_sinh)) # Đếm số cặp key-value phần tử
# # print("Danh sách học sinh sau khi thay đổi:")
# # del danh_sach_hoc_sinh['hs001'] #Xóa phần tử
# # print(danh_sach_hoc_sinh)
# # print(len(danh_sach_hoc_sinh)) # Đếm số cặp key-value phần tử

# #Sử dụng phương thức keys() lấy danh sách key trong Dictionary:
# print("Danh sách các key của Dic: ",danh_sach_hoc_sinh.keys()) 
# #Để chuyển dict_keys thành list dùng hàm list(dict_keys)
# print("Chuyển dict_keys thành list: ",list(danh_sach_hoc_sinh.keys()))
# # Để lấy ra danh sách value của dict dùng phương thức dict.values()
# print("Danh sách giá trị của hs001: ",list(danh_sach_hoc_sinh['hs001'].values()))
# # Kiểm tra 1 key có tồn tại hay không
# if 'hs003' in danh_sach_hoc_sinh:
#     print("Yes")
# else:
#     print("No")
# # Tạo một bản sao của dictionary gốc bằng cách sử dụng hàm copy()
# danh_sach_hoc_sinh['hs003']=danh_sach_hoc_sinh['hs001'].copy()
# print("hs003: ",danh_sach_hoc_sinh['hs003'])
# # Xóa toàn bộ dữ liệu của dict
# print("hs003: ",danh_sach_hoc_sinh['hs003'].clear())

#####################################################################################################################################
# Set là một kiểu dữ liệu trong Python đại diện cho một tập hợp các phần tử duy nhất (Không trùng lặp).
# Không có thứ tự và không thể truy cập thông qua chỉ số.
# Mỗi phần tử trong set phải là duy nhất (không có các phần tử trùng lặp)
# Mỗi phần tử phải là các đối tượng bất biến (immutable) như số nguyên, chuỗi, tuple, v.v.

# # Cách 1: Tạo trực tiếp với dấu {}
# set1={1,2,3,'a','b',True,8.7}
# # Cách 2: Tạo một set và thêm phần tử vào set
# set2=set()
# set2.add(5)
# set2.add('loc')
# set2.add(True)
# # Cách 3: Tạo set từ list và tuple
# list=['a','b',3,1]
# set3=(list)
# my_tuple=tuple([6.7,7,8,6,7,7.6,8,6.9])
# set4=(my_tuple)
# print(set1,set2,set3,set4)

############################################################
# # Union - hợp hai set
# set1={1,2,3}
# set2={4,5,6}
# union_set=set1.union(set2)  #Tạo ra set mới với các phần tử là của 2 set hợp lại, các phần tử không trùng nhau.
# print("Hợp hai set",union_set)

# # Intersection - giao của hai set
# set1={1,2,3,4,5}
# set2={4,5,6}
# intersection_set=set1.intersection(set2) #Tạo ra set mới với các phần tử đều có mặt ở cả 2 set
# print("Giao của hai set",intersection_set)

# # Difference - hiệu của hai set
# #set1 – set2: Lấy ra các phần tử chỉ xuất hiện ở set1 mà không xuất hiện ở set2
# #Cách sử dụng: Có thể sử dụng toán tử "-" hoặc phương thức difference()
# set1={1,2,3,4,5}
# set2={4,5,6}
# diff1=set1-set2
# diff2=set1.difference(set2)
# print(diff1,diff2)

#####################################################################################################################################

#Viết chương trình nhận một câu từ người dùng và đếm số lần xuất hiện của từng từ trong câu. 
#Kết quả sẽ được lưu vào một dictionary, trong đó key là từ và value là số lần xuất hiện của từ đó.
sentence=input("Enter a sentence:")
words=sentence.split()
word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
for word,word_count in word_count.items():
    print(f"{word}: {word_count}")