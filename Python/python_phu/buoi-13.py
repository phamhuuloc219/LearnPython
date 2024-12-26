# 1. Viết chương trình nhập vào số nguyên dương n. Tìm các số chia hết cho 3 và 5 trong khoảng từ 1 đến n
# 2. Viết chương trình tính giá trị của biểu thức S= 1.2 + 2.3 + 3.4 + ... + n(n+1).
# 3. Viết chương trình tính tiền lương khi làm qua số giờ tiêu chuẩn theo quy định của công ty (tăng ca) của 1 nhân viên.
# Biết số giờ tiêu chuẩn là 44 giờ, lương theo giờ là 25$/h. Nếu làm tăng ca thì tính 30$/h. Hãy tính số lương thực lãnh của nhân viên.
# Gợi ý: Đầu vào là 1 số lớn hơn hoặc bằng 44 
# 4. Viết chương trình yêu cầu người dùng nhập vào số đại diện cho ngày trong tuần (1-7).
# Kiểm tra và in ra thông điệp tương ứng với ngày đó (1: Chủ nhật, 2: Thứ hai,...,7: Thứ bảy)







































n = int(input("Nhập n = "))
s = 0

for i in range(1,n+1):
    s += i*(i+1)
print(s)

gio_tieu_chuan = 44
gio_lam = float(input("Nhập số giờ làm thực tế: "))
while gio_lam < 44:
    gio_lam = float(input("Vui lòng nhập lại số giờ làm thực tế: "))
gio_lam_thuc_te = gio_tieu_chuan - gio_lam
luong = gio_tieu_chuan*25 + gio_lam_thuc_te*30

print(f"Số lương thực lãnh của nhân viên là: {luong}")
