danh_ba_dien_thoai = {}

def them_lien_he():
    ten = input("Nhập tên liên hệ: ")
    sdt = input("Nhập số điện thoại: ")
    danh_ba_dien_thoai[ten] = sdt
    print(f"Đã thêm liên hệ: {ten} - {sdt}")

def xoa_lien_he():
    ten = input("Nhập tên liên hệ cần xóa: ")
    if ten in danh_ba_dien_thoai:
        del danh_ba_dien_thoai[ten]
        print(f"Đã xóa liên hệ: {ten}")
    else:
        print(f"Không tìm thấy liên hệ có tên {ten}")

def cap_nhat_lien_he():
    ten = input("Nhập tên liên hệ cần cập nhật: ")
    if ten in danh_ba_dien_thoai:
        sdt_moi = input("Nhập số điện thoại mới: ")
        danh_ba_dien_thoai[ten] = sdt_moi
        print(f"Đã cập nhật liên hệ: {ten} - {sdt_moi}")
    else:
        print(f"Không tìm thấy liên hệ có tên {ten}")

def tim_kiem_lien_he():
    ten = input("Nhập tên liên hệ cần tìm kiếm: ")
    if ten in danh_ba_dien_thoai:
        print(f"Thông tin liên hệ: {ten} - {danh_ba_dien_thoai[ten]}")
    else:
        print(f"Không tìm thấy liên hệ có tên {ten}")

def hien_thi_danh_ba():
    print("Danh bạ điện thoại:")
    for ten, sdt in danh_ba_dien_thoai.items():
        print(f"{ten} - {sdt}")

while True:
    print("\nMenu:")
    print("1. Thêm liên hệ")
    print("2. Xóa liên hệ")
    print("3. Cập nhật liên hệ")
    print("4. Tìm kiếm liên hệ")
    print("5. Hiển thị danh bạ")
    print("6. Thoát")

    lua_chon = input("Chọn chức năng (1-6): ")

    if lua_chon == '1':
        them_lien_he()
    elif lua_chon == '2':
        xoa_lien_he()
    elif lua_chon == '3':
        cap_nhat_lien_he()
    elif lua_chon == '4':
        tim_kiem_lien_he()
    elif lua_chon == '5':
        hien_thi_danh_ba()
    elif lua_chon == '6':
        break
    else:
        print("Chức năng không hợp lệ. Vui lòng chọn lại.")