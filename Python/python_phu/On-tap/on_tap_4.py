# 1. Viết chương trình kiểm tra xem 1 số có phải là số nguyên dương hay không.
# Nếu không phải là số nguyên dương thì yêu cầu người dùng nhập lại. 
# n = int(input("Nhap n = "))
# while n < 0:
#      print("Số nhập phải lớn hơn 0")
#      n = int(input("Nhập lại n = "))
# print("Số nguyên dương vừa nhập là: ", n)

# 2. Viết chương trình kiểm tra mật khẩu "xuanphu". Nếu người dùng nhập sai thì
# yêu cầu người dùng nhập lại. Nếu người dùng nhập đúng mật khau thì in
# ra "Mật khẩu đúng".
# password = "xuanphu".lower()
# mat_khau = input("Nhap mat khau: ").lower()
# while password != mat_khau:
#     print("Sai mat khau")
#     mat_khau = input("Nhap lai mat khau: ").lower()
# print("Mật khẩu đúng")

# 3. Viết chương trình kiểm tra điểm nằm trong khoảng từ 0-10. 
# Nếu không nằm trong khoảng này thì yêu cầu người dùng nhập lại điểm.
# diem = float(input("Nhap diem = "))
# while diem < 0 or diem > 10:
#      print("Điểm nhập phải nằm trong khoảng 0-10")
#      diem = float(input("Nhập lại điểm = "))
# print("Điểm vừa nhập là: ", diem)










def tong( a, b ,c ,d ):
   tong = a + b + c + d
   return tong

def hieu (a , b ,c):
    hieu = a - b - c
    return hieu

def tich (a,b):
    tich = a * b
    return tich
    
def thuong (a,b):
    thuong = a / b
    return thuong

# Tao biến và gọi lại hàm tính tổng hiệu tích thương
total = tong( 10, 20, 50, 100 )
sub = hieu( 10, 20, 50 )
mul = tich( 10, 20 )
div = thuong( 10, 20 )

# in ra màn hình kết quả
print ("Tổng : ", total)
print ("Hieu : ", sub)
print ("Tich : ", mul)
print ("Thuong : ", div)

def xin_chao():
    print("Xin chào!")
    print("Mình là Phạm Hữu Lộc")
    print("Mình là developer của công ty SweetSoft")
