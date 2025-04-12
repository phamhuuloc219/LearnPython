import random

# cho máy chọn 1 trong 3 giá trị là bao/búa/kéo
def may_chon():
    return random.choice(["bao", "búa", "kéo"])

# hàm xử lý người chọn
def nguoi_chon():
    while True:
        nguoi_chon = input("Bạn chọn bao/búa/kéo? ").lower()
        if nguoi_chon in ["bao", "búa", "kéo"]:
            return nguoi_chon
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn bao/búa/kéo: ")
            nguoi_chon = input("Bạn chọn bao/búa/kéo? ").lower()
        
nguoi_chon()