# Khởi tạo từ điển trống để lưu trữ chi tiêu
chi_tieu = {}

def them_chi_tieu():
    # Nhập danh mục chi tiêu và số tiền từ người dùng
    danh_muc = input("Nhập danh mục chi tiêu: ")
    so_tien = float(input("Nhập số tiền: "))

    # Thêm chi tiêu vào từ điển
    if danh_muc in chi_tieu:
        chi_tieu[danh_muc] += so_tien
    else:
        chi_tieu[danh_muc] = so_tien

    print(f"Chi tiêu thêm: {danh_muc} - {so_tien}")

def xem_chi_tieu():
    # Hiển thị tất cả chi tiêu
    print("Chi tiêu:")
    for danh_muc, so_tien in chi_tieu.items():
        print(f"{danh_muc}: {so_tien}")

def tinh_tong_chi_tieu():
    # Tính toán tổng số tiền đã chi
    tong_chi_tieu = sum(chi_tieu.values())
    print(f"Tổng số tiền đã chi: {tong_chi_tieu}")

def main():
    while True:
        print("Quản Lý Chi Tiêu Cá Nhân")
        print("1. Thêm chi tiêu")
        print("2. Xem chi tiêu")
        print("3. Tính tổng chi tiêu")
        print("4. Thoát")

        lua_chon = input("Chọn một tùy chọn: ")

        if lua_chon == "1":
            them_chi_tieu()
        elif lua_chon == "2":
            xem_chi_tieu()
        elif lua_chon == "3":
            tinh_tong_chi_tieu()
        elif lua_chon == "4":
            break
        else:
            print("Tùy chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()