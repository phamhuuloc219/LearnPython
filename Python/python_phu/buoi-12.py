# or: chỉ cần 1 vế đúng
# and: 2 vế đều phải đúng

# xử lý nhập điểm Toán trong khoảng từ 0 đến 10
diemToan = float(input("Nhập điểm toán = "))
while (diemToan < 0 or diemToan > 10):
    diemToan = float(input("Nhập lại điểm toán = "))
    
# xử lý nhập điểm tiếng Anh trong khoảng từ 0 đến 10    
diemTA = float(input("Nhập điểm tiếng Anh = "))
while (diemTA < 0 or diemTA > 10):
    diemTA = float(input("Nhập lại điểm Anh = "))
    
# xử lý nhập điểm tiếng Việt trong khoảng từ 0 đến 10    
diemTV = float(input("Nhập điểm tiếng Việt = "))
while (diemTV < 0 or diemTV > 10):
    diemTV = float(input("Nhập lại điểm tiếng Việt = "))

# tính điểm trung bình
diemTB = (diemToan*2 + diemTA + diemTV*2) / 5
# xử lý xếp loại học sinh
if (diemTB >= 8 and diemTB <=10):
    print("Xếp loại: Giỏi")
elif (diemTB >= 6.5 and diemTB < 8):
    print("Xếp loại: Khá")
elif (diemTB >= 5 and diemTB < 6.5):
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")
    
# 5. Viết chương trình nhập vào điểm Toán, Tiếng Anh và Tiếng Việt
# và tính điểm trung bình.
# Giỏi (DTB >= 8 and DTB <=10)
# Khá (DTB >= 6.5 and DTB < 8)
# Trung Bình (DTB >= 5 and DTB < 6.5)
# Yếu (DTB >=0 and DTB < 5 )

# 1.  Nhập vào hai số nguyên dương a và b. Tìm tổng của tất cả các số lẻ
# và chẵn nằm giữa hai số đó.(Gợi ý: Tạo 2 biến tongLe và tongChan)
# a= int(input("a= "))
# while(a<0):
# 	a = int(input("a= "))
# b= int(input("b= "))
# while(b<0):
# 	b = int(input("b= "))
# while(a>b):
#     print("Nhập lại a bắt buộc phải bé hơn b !!!")
#     a = int(input("a= "))
    
# tongLe = tongChan = 0

# for i in range(a,b+1):
# 	if i%2==0:
# 		tongChan += i
# 	else:
# 		tongLe +=i
  
# print("Tổng các số chẵn là: ", tongChan)
# print("Tổng các số lẻ là: ", tongLe)
# 2. Viết chương trình yêu cầu người dùng đoán một số bí mật trong khoảng từ 1 đến 100. 
# Chương trình sẽ tiếp tục yêu cầu người dùng đoán cho đến khi họ đoán đúng. 
# Mỗi lần đoán, chương trình sẽ cho biết số người dùng đoán là lớn hơn hay nhỏ hơn số bí mật.
# number_secret = 219
# n = int(input("Nhập số bí mật: "))
# while n != number_secret:
# 	if n > number_secret:
# 		print("Số bạn nhập vào lớn hơn số bí mật")
# 	elif ((n > (number_secret-10)) and (n < (number_secret+10))):
# 			print("Số bạn nhập vào gần đúng với số bí mật")
# 	elif (n < number_secret):
# 		print("Số bạn nhập vào nhỏ hơn số bí mật")
# 	n = int(input("Nhập số bí mật: "))
# print("Số bạn nhập vào đúng với số bí mật")
# 3. Nhập 2 số nguyên x và y. Viết chương trình tính tổng bình phương các số từ x đến y.
a = int(input("a= "))
b = int(input("b= "))
tong = 0
for i in range(a,b+1):
	tong += i**2

print("Tong binh phuong cua cac so tu",a,"den",b,"la:",tong)