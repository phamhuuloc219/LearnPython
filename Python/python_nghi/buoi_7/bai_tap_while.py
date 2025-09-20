# Bài 1: 1.Viết một chương trình Python để phân loại học sinh theo điểm 
# thi trung bình cộng 3 môn Toán-Lý-Hóa, với Toán là môn nhân hệ số 2. 
# Điều kiện là chương trình sẽ nhập 3 điểm thi của học sinh (số thực từ 0 đến 10)
# và in ra xếp loại tương ứng dựa trên thang điểm sau: Giỏi: 8.0 - 10.0: 
# Khá: trên 6.5 đến dưới 8.0: Trung bình: trên 4.5 đến dưới 6.5: 
# Yếu: từ 0 đến dưới 4.5

# 2. Viết chương trình yêu cầu người dùng đoán một số bí mật trong khoảng từ 1 đến 100.
# Chương trình sẽ tiếp tục yêu cầu người dùng đoán cho đến khi họ đoán đúng.
# Mỗi lần đoán, chương trình sẽ cho biết số người dùng đoán là lớn hơn hay 
# nhỏ hơn số bí mật.

# import random # sử dụng mô-đun random để có thể sinh ra số ngẫu nhiên

# so_bi_mat = random.randint(1,100) # số bí mật được sinh ra ngẫu nhiên từ 1 đén 100
# # nhập số vào
# number = int(input("Nhập số bí mật: "))
# while number != so_bi_mat:
#     if (so_bi_mat - 5) <= number <= (so_bi_mat + 5):
#         print("Số bạn nhập vào gần bằng số bí mật")
#         number = int(input("Nhập số bí mật: "))
#     elif number > so_bi_mat:
#         print("Cao quá ~ Thử lại!")
#         number = int(input("Nhập số bí mật: "))
#     elif number < so_bi_mat:
#         print("Thấp quá~ Thử lại!")
#         number = int(input("Nhập số bí mật: "))
# print("Bạn đoán đúng rồi <3")




# bài 4
n = int(input("Nhập n = "))
so_ban_dau = n
dem = 0
while n < 0:
    n = int(input("Nhập lại n = "))

while n > 0:
    n = n // 10
    dem += 1
print(f"Số {so_ban_dau} có {dem} chữ số")