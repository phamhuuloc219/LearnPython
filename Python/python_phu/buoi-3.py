"""

Bài tập 1: Tính tổng hai số
   - Yêu cầu người dùng nhập vào hai số và in ra tổng của chúng.
   
Bài tập 2: Chuyển đổi nhiệt độ
   - Yêu cầu người dùng nhập vào một số đo nhiệt độ ở độ C
   và chuyển đổi sang độ F, sau đó in ra kết quả. 
   Độ F = (Độ C × 9/5) + 32 
   
   

Bài tập 3: Tính diện tích hình chữ nhật
   - Yêu cầu người dùng nhập vào chiều dài và chiều rộng của hình chữ nhật,
   sau đó tính diện tích và in ra kết quả.

Bài tập 4: Tính chỉ số BMI
   - Yêu cầu người dùng nhập vào cân nặng (kg) và chiều cao (m), 
   sau đó tính chỉ số BMI (Body Mass Index) và in ra kết quả.

Bài tập 5: Tính diện tích hình tròn
   - Yêu cầu người dùng nhập vào bán kính hình tròn, 
   sau đó tính diện tích và in ra kết quả.
   
"""

# # Bài 1
# a = int(input("Nhập số thứ nhất = "))
# b = int(input("Nhập số thứ hai = "))
# tong = a + b
# print("Tổng hai số = ", tong)

# # Bai 2
# C = float(input("Nhập độ C = ")) # 33.2
# F = C * 9/5 + 32
# print(C,"C degree = ",F,"F degree")

# # bai 3
# chieu_dai = int(input("Nhập chiều dài = "))
# chieu_rong = int(input("Nhập chiều rộng = "))
# dien_tich = chieu_dai * chieu_rong
# print("Diện tích hình chữ nhật = ", dien_tich)

# # Bai 4
# # BMI = cân nặng (kg) / chiều cao² (m)
# can_nang = float(input("Nhập cân nặng = "))
# chieu_cao = float(input("Nhập chiều cao = "))
# bmi = can_nang / chieu_cao**2
# print("Chỉ số BMI là: ", bmi)    

# Bai 5
pi = 3.14
ban_kinh = float(input("Nhập bán kính hình tròn = "))

dien_tich = pi * ban_kinh**2
print("Diện tích hình tròn = ", dien_tich)

chu_vi = 2 * ban_kinh * pi
print("Chu vi hình tròn = ", chu_vi)