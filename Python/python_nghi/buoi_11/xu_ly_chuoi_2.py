# name = input("Nhập tên của bạn: ").strip() # Loại bỏ khoảng trắng ở 2 đầu
# print("\'",name,"\'")
# print("In hoa:","\'",name.upper(),"\'") # upper viết hoa tất cả
# print("In thuong:","\'",name.lower(),"\'") # lower viết thường tất cả


text = "xyn trao cac banj toi laf python"
print("text ban dau: ",text)
print("thay the lan 1: ",text.replace("xyn", "xin"))
print("thay the lan 2: ",text.replace("trao", "chao"))

new_text = text.replace("xyn", "xin").replace("trao", "chao")

print("thay the lan 3: ",new_text)