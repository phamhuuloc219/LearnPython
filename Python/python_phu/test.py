# Giá bán cam tại siêu thị tính như sau: nếu khối lượng cam mua dưới 5kg
# thì giá bán là 12 000 đồng/kg, nếu khối lượng mua lớn hơn hoặc bằng 5kg
# thì giá bán là 10 000 đồng/kg. Viết chương trình nhập số lượng mua (tính theo kg)
# sau đó tính số tiền phải trả.

# sl = float(input("Nhập số lượng cam muốn mua: "))
# tong_tien = 0.0

# if sl >= 5:
#     tong_tien = 10000 * sl
# elif sl <5 and sl >= 0:
#     tong_tien = 12000 * sl
# else:
#     print("Số kg phải lớn hơn hoặc bằng 0")
    
# print("Tổng tiền bạn cần trả là: ", tong_tien)

import datetime
name = input("Nhap ho ten: ")
dob = int(input("nhap tuoi: "))
print(f"xin chao {name} ban {datetime.datetime.now().year - dob} tuoi")