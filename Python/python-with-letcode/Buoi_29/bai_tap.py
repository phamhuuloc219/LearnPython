# import my_math
# total = my_math.tong(5,10)
# print (total)

# subtraction = my_math.tru(10,5)
# print ('hieu=', subtraction)

# mod = my_math.chia(10,5)
# print ('chia =', mod)

# nhan = my_math.nhan(10,5)
# print ('nhan =', nhan)

# # "Bài Tập 1: Tính Căn Bậc Hai
# # Sử dụng module math, viết một chương trình yêu cầu người dùng nhập một số và in ra căn bậc hai của số đó.
# import math
# print (math.sqrt(9))
# # Bài Tập 2: Tính Diện Tích Hình Tròn
# # Sử dụng module math, viết một chương trình yêu cầu người dùng nhập bán kính của hình tròn và tính diện tích của hình tròn đó.
# import math
# print (math.pi)
# # Bài Tập 3: Sinh Số Ngẫu Nhiên
# # Sử dụng module random, viết một chương trình in ra một số nguyên ngẫu nhiên từ 1 đến 100.
# import random
# a = random.randint(1,100)    
# b = random.randint(1,10)
# print (a)
# print(b)
# # Bài Tập 4: Chọn Ngẫu Nhiên Từ Danh Sách
# # Sử dụng module random, viết một chương trình chứa một danh sách các tên và in ra một tên ngẫu nhiên từ danh sách đó.
# import random
# a = ['Lam', 'Phu', 'Dang', 'Bao', 'Loc', 'Phong']
# b = random.randrange(len(a))
# print (a[b])
# # Bài Tập 5: Tính Ngày Hôm Sau
# # Sử dụng module datetime, viết một chương trình in ra ngày hôm sau của ngày hiện tại.

# # Bài Tập 6: Tính Tuổi
# # Sử dụng module datetime, viết một chương trình yêu cầu người dùng nhập ngày sinh của họ và tính tuổi của họ.

# # Bài Tập 7: Đếm Ngược Thời Gian
# # Sử dụng module datetime, viết một chương trình đếm ngược từ 10 giây xuống 0 và in ra “Time’s up!” khi hết giờ.

# # Bài Tập 8: In Các Đối Số Dòng Lệnh
# # Sử dụng module sys, viết một chương trình in ra tất cả các đối số dòng lệnh đã nhập vào khi chạy chương trình.

# # Bài Tập 9: Kiểm Tra Phiên Bản Python
# # Sử dụng module sys, viết một chương trình in ra phiên bản Python hiện tại đang được sử dụng.

# # Bài Tập 10: Kiểm Tra Đường Dẫn Python
# # Sử dụng module sys, viết một chương trình in ra đường dẫn của trình thông dịch Python đang được sử dụng."




# import my_math
# import my_math as mm

# tong = my_math.tong(4,6)
# hieu = my_math.tru(6,4)
# thuong = mm.chia(4,5)
# print ("tong la : ",tong)
# print ("hieu la : ",hieu)


# import math

# can_hai = math.sqrt(25)
# luy_thua = pow(5, 6)
# tri_tuyet_doi = abs(-99)

# so_pi = round(math.pi,5)

# print(can_hai)
# print(luy_thua)
# print(tri_tuyet_doi)
# print(so_pi)

import random
# so = random.randint(1,100)
# b = random.uniform(1,2)
# so_ngau_nhien = random.randrange(1,100,2)
# a = random.seed(50)

# print(so)
# print(b)
# print(so_ngau_nhien)

# hello = random.choice(["a","b","c"])
# print(hello)

# import datetime

# # gio_hien_tai = datetime.datetime.now().strftime("%H:%S:%M") # hour: min : sec
# # print(gio_hien_tai)

# birthdate = input("Nhap ngay sinh nhat (YYYY-MM-DD): ")
# birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
# print("ngay sinh nhat cua toi: ",birthdate)

# from datetime import datetime, timedelta

# current_date = datetime.now()
# next_day = current_date + timedelta(days=-4000,weeks=2,hours=1)

# print("Ngày mai là:", next_day) # Ngày mai là: 2013-09-12 23:09:04.547941