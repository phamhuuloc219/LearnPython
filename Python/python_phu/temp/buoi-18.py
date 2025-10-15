#1. Hàm in ra màn hình
# print("Nội dung")

#2. Hàm làm tròn số thập phân
# round(số cần làm tròn, làm tròn đến số thứ mấy sau dấu phẩy) 
# a = 3.1415926535897
# print(round(a,4))

#3. ép kiểu
# int(): chuyển kiểu dữ liệu sang kiểu số nguyên
# a = 10.9923
# b = int(a)
# print(b)
# # float(): chuyển kiểu dữ liệu sang kiểu số thực(số thập phân)
# a = 6
# b = float(a)
# print(b)

#4. Hàm range()
# range(start, stop, step)

#5. Hàm abs(): kết quả trả về luôn luôn là 1 số dương
# print(abs(-47298384))

#6, Hàm pow(): lũy thừa
# print(pow(4,5))

#7. Hàm sum()
# list= [1,6,3,6,7,2,9,33]
# print(sum(list))
# print(max(list))
# print(min(list))

#8 Hàm sắp xếp sorted() sắp xếp từ bé đến lớn
# print(sorted(list))
# # sắp xếp từ lớn đến bé
# print(sorted(list, reverse=True))


# Cú pháp khởi tạo hàm
# def tên_hàm():
    # <Câu lệnh>

def xin_chao():
    print("Xin chào!")

xin_chao()


def tinh_tong(a, b):
    print("Tong= ",a + b) 

a = int(input("a= "))
b = int(input("b= "))  
tinh_tong(a,b)


#Phan dinh nghia ham
def thong_bao(SBD,Ten,Age=10):
    print(SBD)
    print(Ten)
    print(Age)
    return
#Function call
thong_bao(101,'Phú')
print("============================================================")
thong_bao(102,'Tiền',12)