# Module trong python
# nhiều "hàm" => 1 "module"
# Nhiều "module" => 1 "package"
# Nhiều "package" => 1 "lib" (thư viện)
# Nhiều "lib" => 1 "framework"

# 1. Giới thiệu về phân chia mã trong Python
# Module: các đoạn mã nhỏ, từ chứa đựng có thể được import và tái sử dụng
# packages: 1 tập hợp các module được lưu trữ trong các mục 
# Libraries: 1 tập hợp các package cung cấp nhiều chức năng đa dạng
# Frameworks: các bộ sưu tập lớn hơn của libraries và packages được thết kế cho các mục đích cụ thể (vd: phát triển web, khoa học dữ liệu)

# 2. Nhóm Các Mã Thành Module và Sử Dụng Import
# Tạo một module bằng cách lưu các hàm vào một tệp .py.
# Import một module bằng câu lệnh import .
# Hoạt động:
# Tạo một module tên là my_math.py chứa các hàm cho phép cộng, trừ, nhân, và chia.
# Import module vào một tệp Python khác và sử dụng các hàm trong đó.

# random: Tạo số ngẫu nhiên.
# math: Thực hiện các phép toán nâng cao.
# datetime: Làm việc với ngày và giờ.
# sys: Tương tác với trình thông dịch Python.
# import math
# # lũy thừa
# print(pow(3, 2))
# # Căn bậc 2
# print(math.sqrt(9))
# # trị tuyệt đối
# print(abs(-5))

# import random
# a = random.randint(1, 100)
# b = random.randrange(1, 100)
# print(a)
# print(b)

# import sys
# def check_platform():
#     platform_name = sys.platform
#     if platform_name == 'win32':
#         print('platform: Windows')
#     elif platform_name == 'linux':
#         print('platform: Linux')
#     elif platform_name == 'darwin':
#         print('platform: MacOS')
#     else:
#         print('platform: Unknow')
# check_platform()

import datetime
# #"datetime.date": Đại diện cho ngày tháng(năm, tháng, ngày)
today = datetime.date.today()
print (today)
#"datetime.time": đại diện cho giờ phút ( giờ, phút, giây, microsecond)
time_now = datetime.time(10,20,50,00)
print (time_now)
#"datetime.datetime": kết hợp cả ngày tháng và thời gian 
time_now = datetime.datetime.now()
print (time_now)
#"datetime.timedelta": Đại diện cho khoảng thời gian (sự khác biệt giữa 2 thời điểm)
delta = datetime.timedelta(days=10)
future_date = today +delta
print(future_date)
