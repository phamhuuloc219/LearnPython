def tinh_diem_trung_binh(diem):
    return sum(diem) / len(diem)

def xep_loai(diem_tb):
    if diem_tb >= 8:
        return "Giỏi"
    elif diem_tb >= 6.5:
        return "Khá"
    elif diem_tb >= 5:
        return "Trung bình"
    else:
        return "Yếu"

hoc_sinh = {}

so_hoc_sinh = int(input("Nhập số học sinh: "))
for i in range(so_hoc_sinh):
    ten = input("Nhập tên học sinh: ")
    diem = list(map(float, input("Nhập điểm của học sinh (cách nhau bởi dấu cách): ").split(",")))
    hoc_sinh[ten] = diem

print("\nBáo cáo kết quả:")
for ten, diem in hoc_sinh.items():
    diem_tb = tinh_diem_trung_binh(diem)
    xep_loai_hoc_luc = xep_loai(diem_tb)
    print(f"{ten}: Điểm trung bình = {diem_tb:.2f} - Xếp loại: {xep_loai_hoc_luc}")