#1. Viết chương trình nhập vào điểm của học sinh và
# xếp hạng học lực của học sinh dựa trên:
# - Điểm trung bình >= 9.0 và < 10 là Xuất sắc.
# - Điểm trung bình >=7.0 và < 9.0 là Giỏi
# - Điểm trung bình >5.0 và < 7.0 là Khá
# - Điểm trung bình >=3.5 và <= 5.0 là Trung Bình
# - Điểm trung bình <3.5 là Yếu
# diem = float(input("Diem = "))
# if diem >= 9 and diem <= 10:
#     print("Xuat sac")
# elif diem >=7 and diem < 9:
#     print("Gioi")
# elif diem >=5 and diem < 7:
#     print("Kha")
# elif diem >= 3.5 and diem < 5:
#     print("trung binh")
# elif diem >= 0 and diem < 3.5:
#     print("Yeu")
# else:
#     print("Ban nhap diem khong hop le. Vui long nhap lai")
# 2. Viết chương trình tìm số chia hết cho 3

# n = int(input("nhap N= "))
# if(n % 3 == 0):
#     print(n,"la so chia het cho 3")
# else:
#     print(n,"khong la so chia het cho 3")

# 3. Viết chương trình tìm số chia hết cho 5 và 7

# n = int(input("nhap N= "))
# if(n % 5 == 0 and n % 7 == 0):
#     print(n,"la so chia het cho 5 va 7")
# else:
#     print(n,"khong la so chia het cho 5 va 7")
    
# 4. Viết chương trình tìm số chẵn và chia hết cho 3

n = int(input("Enter the number: "))
if (n % 2 == 0):
    if (n % 3 == 0):
        print(n," là số chẵn và chia hết cho 3")
    else:
        print(n," là số chẵn và không chia hết cho 3")
else:
    print(n," không phải là số chẵn")
