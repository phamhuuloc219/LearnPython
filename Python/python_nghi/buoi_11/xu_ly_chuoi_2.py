# name = input("Nhập tên của bạn: ").strip() # Loại bỏ khoảng trắng ở 2 đầu
# print("\'",name,"\'")
# print("In hoa:","\'",name.upper(),"\'") # upper viết hoa tất cả
# print("In thuong:","\'",name.lower(),"\'") # lower viết thường tất cả


# text = "xyn trào các banj tôi laf python"
# print("text ban dau: ",text)

# new_text = text.replace("xyn", "xin").replace("trào", "chào").replace("banj", "bạn").replace("laf", "là")

# print("Kết quả: ",new_text)

text = input("Nhập văn bản: ").strip()
# liệt kê tất cả kí tự đặc biệt muốn lọc ra
specialChars = "~`!@#$%^&*()-+_={}[]\\|;:\"\'<>,.?/"

for char in special_chars:
    text = text.replace(char, "")

print(text)