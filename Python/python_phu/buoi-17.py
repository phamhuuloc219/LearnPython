# Bài 1: cho 1 chuỗi ký tự :"xin chà@o tấ&t c!ả c$ác b*ạn h#ôm n?ay mình h~ọc python"
# sử dụng hàm replace() để xóa các ký tự đặc biệt
# # Cách 1:
# s1 = "xi?n chà@o tấ&t c!ả c$ác b*ạn h#ôm n?ay mình h~ọc python"
# s_new = ' '.join(c for c in s1 if c.isalnum())
# print(s_new)
# # Cách 2:
# special_char2 = ["~","!","@","#","$","%","^","&","*","?",".",",",";",":"]
# s = "xi?n chà@o tấ&t c!ả c$ác b*ạn h#ôm n?ay mình h~ọc python"
# for char in s:
#     if char in special_char2:
#         s = s.replace(char, "")
# print(s)




# Bài 2: Cho 1 chuỗi ký tự: "mango;banana;burger;cherry;cheese". 
# Tách chuỗi đã cho thành 1 danh sách và in ra phần tử thứ nhất và phần tử thứ ba
s = "mango;banana;burger;cherry;cheese"
s_new = s.split(";")

print(s_new[0])
print(s_new[2])