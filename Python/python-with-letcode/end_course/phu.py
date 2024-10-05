#Chủ đề 1: Quản lý điểm số của học sinh
#đề bài:
#Mô tả: Tạo một chương trình quản lý điểm số của học sinh với chức năng nhập điểm,
#tính điểm trung bình, xếp loại và in báo cáo kết quả.
#Yêu cầu: Sử dụng cấu trúc dữ liệu phù hợp để lưu trữ thông tin học sinh và điểm số,
#hiển thị kết quả có định dạng rõ ràng.
#=========================================================================================
#                                  Bài làm:
hoc_sinh= {}
diem_so = None
def them_diem_so(diem_so):
    so_hoc_sinh=int(input("nhập số học sinh: "))
    for i in range(so_hoc_sinh):
        ten=input("Nhập họ vào tên: ")
        diem_so=list(map(float,input("nhập điểm của bạn (cách nhau bằng dấu phẩy): ").split(",")))
        for i in diem_so:
            while i < 0 or i>10:
                print("vui lòng nhập lại: ")
                diem_so=list(map(float,input("nhập điểm của bạn (cách nhau bằng dấu phẩy): ").split(",")))
        hoc_sinh[ten]=diem_so
        print("đã thêm thông tin thành công!")
def tinh_diem_tb(diem_so):
    return sum(diem_so) / len(diem_so)
def xep_loai(diemtb):
    if diemtb>=9:
        return "Xuất sắc"
    elif diemtb >=8:
        return "giỏi"
    elif diemtb>=6:
        return "khá"
    elif diemtb>=5:
        return "trung bình"
    else:
        return "yếu"
def bao_cao_ket_qua(diem_so):
    for ten,diem_so in hoc_sinh.items():
        diemtb = tinh_diem_tb(diem_so)
        ket_qua=xep_loai(diemtb)
        print(f"{ten} điểm trung bình là : {diemtb}, kết quả học tập là: {ket_qua}")
def menu():
    global diem_so
    while True:
        print("----Chương trình nhập điểm học sinh----")
        print("1. nhập tên,điểm của học sinh")
        print("2. Xem kết quả")
        print("3. thoát")
        lua_chon=int(input("nhập lựa chọn của bạn (1-3): "))
        if lua_chon == 1:
            them_diem_so(diem_so)
        elif lua_chon == 2:
            bao_cao_ket_qua(diem_so)
        elif lua_chon == 3:
            break
menu()