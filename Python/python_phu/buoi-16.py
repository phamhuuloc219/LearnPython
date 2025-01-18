# replace() thay thế một chuỗi bằng một chuỗi khác
s = "@python!@!$%^&* is@ fun"
# thay thế n thành w
s = s.replace("@", "").replace("!","").replace("$", "").replace("%","")
print(s)

# Hàm split() tách chuỗi thành danh sách theo ký tự
str = "mango banana burger cherry cheese"
str1 = str.split("a")
print(str1)

str = "mango banana burger cherry cheese"
print(str.find("b"))

# Bài 1: cho 1 chuỗi ký tự :"xin chà@o tấ&t c!ả c$ác b*ạn h#ôm n?ay mình h~ọc python"
# sử dụng hàm replace() để xóa các ký tự đặc biệt

# Bài 2: Cho 1 chuỗi ký tự: "mango;banana;burger;cherry;cheese". 
# Tách chuỗi đã cho thành 1 danh sách và in ra phần tử thứ nhất và phần tử thứ ba