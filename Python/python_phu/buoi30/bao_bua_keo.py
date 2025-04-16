import random

# Hàm xử lý cho máy chọn 1 trong 3 giá trị là bao/búa/kéo
def may_chon():
    return random.choice(["bao", "búa", "kéo"])

# hàm xử lý người chọn
def nguoi_chon():
    nguoi_chon = input("Chọn búa, bao, kéo:  ").lower()
    while nguoi_chon not in ["bao", "búa", "kéo"]:
        print("Lựa chọn không hợp lệ. Vui lòng chọn búa, bao hoặc kéo.")
        nguoi_chon = input("Chọn búa, bao, kéo:  ").lower()
    return nguoi_chon
        
def thi_dau():
    may = may_chon()
    nguoi = nguoi_chon()
    print("Máy ra",may)
    print("Người ra",nguoi)
    if(
           (nguoi == 'bao' and may == 'búa')
        or (nguoi == 'búa' and may == 'kéo') 
        or (nguoi == 'kéo' and may == 'bao')
        ):
        print("=> Người thắng")
    elif nguoi == may :
        print("=> Hòa")
    else: 
        print("=> Người thua")

# chay chuong trinh
thi_dau()