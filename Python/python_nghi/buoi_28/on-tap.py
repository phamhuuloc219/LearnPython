# 3. Viết hàm kiểm tra số nguyên tố
# Gợi ý: Vòng lặp for, kiểm tra nếu n chia từ 1 đến n

# 4. Viết hàm tính tiền điện theo bậc thang (if-else)
# Ví dụ:
# - 0–50 kWh
# - 51–100 kWh
# - 100 kWh
def tinh_tien_dien(so_kwh):
    tien = 0
    if so_kwh <= 50: # 0 - 50
        tien = so_kwh * 1984
    elif so_kwh <= 100: # 51 - 100
        tien = 50 * 1984 + (so_kwh - 50 ) * 2050
    elif so_kwh <= 200: # 101 - 200
        tien = 50 * 1984 + 50 * 2050 + (so_kwh - 100) * 2380
    elif so_kwh <= 300: # 201 - 300
        tien = 50 * 1984 + 50 * 2050 + 100 * 2380 + (so_kwh - 200) * 2998
    elif so_kwh <= 400: # 301 - 400
        tien = 50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + (so_kwh - 300) * 3350
    elif so_kwh > 400: # trên 400
        tien = 50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + 100 * 3350 + (so_kwh - 400) * 3460
    else:
        return "Số kWh không hợp lệ"
    
    return tien


# 6. Viết hàm đếm số ký tự nguyên âm trong chuỗi

# 7. Viết hàm chuẩn hóa họ tên (viết hoa chữ cái đầu)

# 8. Viết hàm đảo ngược chuỗi. Không dùng cú pháp [::-1].