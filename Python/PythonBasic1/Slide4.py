# def tong(a,b):
#     tong=a+b
#     return tong
# x=5
# y=10
# s=tong(x,y)
# print("Tong cua x ",x," va y ",y," la: ",s)


################################################################
# str="""line 1
# line 2
# line 3
# line 4"""
# # print(str)
# # print(str[0:6]) #in ra line 1
# # print(str[7:]) #in ra bat dau tu line 2 -> het
# # print(len(str)) #dem ky tu
# new_str=str.replace("line 1","Line 1 sau khi thay the") # thay the
# print(new_str)

################################################################
#Tìm vị trí chuỗi
# chuoi_cha="hello, world!"
# chuoi_con="world"
# vi_tri=chuoi_cha.find(chuoi_con) # tìm chuỗi con trong chuỗi cha, nếu không tìm thấy trả về -1
# if vi_tri != -1:
#     print(f"Chuỗi con '{chuoi_con}' được tìm thấy ở vị trí {vi_tri}")
# else:
#     print("Không tìm thấy chuỗi con trong chuỗi cha!!!")


################################################################
#Tách chuỗi thành danh sách
# Fruits="apple,orange,banana,mango"
# List=Fruits.split(",") # Chuyển chuỗi thành danh sách
# print(List)


################################################################
#Xóa khoảng trắng ở đầu và cuối chuỗi
# str="    Hello    "
# print(str)
# chuoi_da_trim= str.strip() # Xóa khoảng trắng ở đầu và cuối chuỗi
# print(chuoi_da_trim)

# chuoi_trim_dau=str.lstrip() # Xóa khoảng trắng ở đầu
# print(chuoi_trim_dau)

# chuoi_trim_cuoi=str.rstrip() # Xóa khoảng trắng ở cuối 
# print(chuoi_trim_cuoi)


################################################################
#Chuyển chuỗi thành in hoa và thường
# chuoi="Hello, World"
# chuoi_thuong=chuoi.lower()
# chuoi_hoa=chuoi.upper()
# print(chuoi_thuong)
# print(chuoi_hoa)



################################################################

cha=str(input("Enter a sentence: ")) #There are two people in my house, they are werewolves
con=str(input("Enter a word to count: "))
dem=0
chuoi=cha.split()
for i in chuoi:
    if i ==con:
        dem+=1
print(f"The word {con} appeared {dem} times in the sentence")