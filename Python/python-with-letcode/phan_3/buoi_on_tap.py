# Danh bạ điện thoại
danh_ba = {}

def them_lien_he():
    ten = input("Nhập tên: ")
    sdt = input("Nhập số điện thoại: ")
    danh_ba[ten] = sdt
    print(f"Đã thêm liên hệ: {ten} - {sdt}")

def xem_danh_ba():
    if len(danh_ba) == 0:
        print("Danh bạ rỗng.")
    else:
        print("Danh bạ điện thoại:")
        for ten, sdt in danh_ba.items():
            print(f"Tên: {ten}, Số điện thoại: {sdt}")

def xoa_lien_he():
    ten = input("Nhập tên cần xóa: ")
    if ten in danh_ba:
        del danh_ba[ten]
        print(f"Đã xóa liên hệ {ten}.")
    else:
        print(f"Không tìm thấy {ten} trong danh bạ.")

def sua_lien_he():
    ten = input("Nhập tên cần sửa: ")
    if ten in danh_ba:
        sdt_moi = input("Nhập số điện thoại mới: ")
        danh_ba[ten] = sdt_moi
        print(f"Đã cập nhật số điện thoại của {ten} thành {sdt_moi}.")
    else:
        print(f"Không tìm thấy {ten} trong danh bạ.")

def menu():
    while True:
        print("\n--- Quản lý danh bạ ---")
        print("1. Thêm liên hệ")
        print("2. Xem danh bạ")
        print("3. Sửa liên hệ")
        print("4. Xóa liên hệ")
        print("5. Thoát")
        lua_chon = input("Chọn chức năng (1-5): ")

        if lua_chon == '1':
            them_lien_he()
        elif lua_chon == '2':
            xem_danh_ba()
        elif lua_chon == '3':
            sua_lien_he()
        elif lua_chon == '4':
            xoa_lien_he()
        elif lua_chon == '5':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

menu()
student ={"name":"Loc", "class":"NTU","Address":""}
print(student)
student["Address"] = "Nha trang"
print(student)