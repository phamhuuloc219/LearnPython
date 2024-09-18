# Trong Python, một module là một file chứa mã Python, có thể bao gồm các định nghĩa về hàm, lớp, và biến, cũng như các đoạn mã thực thi.
# Modules giúp tổ chức mã nguồn thành các phần nhỏ hơn, dễ quản lý hơn, và cho phép tái sử dụng mã ở nhiều chương trình khác nhau.
# Module trong python
# Nhiều "hàm" -> 1 "module"
# Nhiều module -> 1 "packages"
# Nhiều "packages" -> 1 "lib" (thư viên)
# Nhiều "lib" -> 1 "framework"
# 1. Giới Thiệu Về Phân Chia Mã Trong Python
# Modules: Các đoạn mã nhỏ, tự chứa đựng có thể được import và tái sử dụng.
# Packages: Một tập hợp các module được lưu trữ trong các thư mục.
# Libraries: Một tập hợp các package cung cấp nhiều chức năng đa dạng.
# Frameworks: Các bộ sưu tập lớn hơn của libraries và packages được thiết kế cho các mục đích cụ thể(ví dụ: phát triển web, khoa học dữ liệu).
# 2. Nhóm Các Mã Thành Module và Sử Dụng Import
# Tạo một module bằng cách lưu các hàm vào một tệp .py.
# Import một module bằng câu lệnh import .
# Hoạt động:
# Tạo một module tên là my_math.py chứa các hàm cho phép cộng, trừ, nhân, và chia.
# Import module vào một tệp Python khác và sử dụng các hàm trong đó.
# import my_math
# print(my_math.greet("Loc"))
# tong = my_math.add(5,3)
# hieu = my_math.sub(7,1)
# print(f"tong = {tong} vaf hieu = {hieu}")
import sys
import datetime

def check_platform():
    platform_name = sys.platform
    if platform_name == "win32":
        return print("Windows")
    elif platform_name == "darwin":
        return print("MacOS")
    elif platform_name == "linux":
        return print("Linux")
    else:
        return print("Unknown")
check_platform()

today = datetime.datetime.today()
timee = datetime.datetime.now()
print(timee)

