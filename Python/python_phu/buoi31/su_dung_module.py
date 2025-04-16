# from toan_hoc import phep_Cong, phep_Tru

# if __name__ == "__main__":
#     a = int(input("Nhap a: "))
#     b = int(input("Nhap b: "))

#     ket_qua_phep_cong = phep_Tru()
#     print(ket_qua_phep_cong)


# lấy hết tất cả các hàm trong module
import random
# lấy cụ thể hàm nào trong module (Tối ưu hơn)
from random import choice, randint

print(choice(["bao", "búa","kéo",6,10.6, True]))