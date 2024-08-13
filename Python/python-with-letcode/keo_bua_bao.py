import random

def nguoi_choi():
    nhap_keo_bua_bao = input("chon keo, bua, bao: ").lower()
    while nhap_keo_bua_bao not in ["bao","bua","keo"]:
        print("khong hop le")
        nhap_keo_bua_bao = input("chon keo, bua, bao").lower()
    return nhap_keo_bua_bao

def nguoi_may():
    return random.choice(["bao","bua","keo"])

def ket_qua(nguoi_choi, may_choi):
    if nguoi_choi == may_choi:
        return "Hoa"
    elif (nguoi_choi == "keo" and may_choi == "bua") or (nguoi_choi == "bua" and may_choi == "bao") or (nguoi_choi == "bao" and may_choi == "keo"):
        return "Ban Thua"
    else:
        return "Ban Thang"

user = nguoi_choi()
computer = nguoi_may()
print("Lựa chọn của bạn: ",user)
print("Lựa chọn của máy:", computer)
print(ket_qua(user,computer))