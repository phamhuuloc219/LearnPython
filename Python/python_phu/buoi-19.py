# 1, Viết hàm yêu cầu người dùng nhập họ tên rồi đưa lời chào ra màn hình
# input:Phu => Xin chào Phú
# 2. Viết hàm kiểm tra số chẳn hoặc lẻ với n là số nguyên dương người dùng nhập
# từ bàn phím rồi in kết quả ra màn hình

def chan_le(n):
    if n % 2 == 0:
        return "Số chẵn"
    else:
        return "Số lẻ"
    
n = int(input("Nhập 1 số nguyên dương: "))
while n < 0:
    n = int(input("Hãy nhập 1 số nguyên dương: "))  
    
print(chan_le(n))
# 3. Viết hàm tính giá trị trung bình của 4 số nguyên dương được người dùng nhập
# từ bàn phím rồi in kết quả ra màn hình
# 4. Viết hàm tìm số lớn nhất của hai số nguyên dương được người dùng nhập từ bàn 
# phím rồi in kết quả ra màn hình


# Dựa vào hàm tính tổng
def tinh_tong(m, n):
    print("Tong= ",n + m) 

# a = int(input("a= "))
# b = int(input("b= "))  

# tinh_tong(a,b)

# def tinh_thuong(a,b):
#     if b == 0:
#         print("Vui lòng nhập  số b khác 0")
#     else:
#         print("thuong= ", a / b)
# Viết hàm tính hiệu, tích,
# thương(b!=0 thì sẽ chia được, còn b==0 thì không chia được)




def so_sanh(a,b):
    if a > b:
        return a
    else:
        return b
a = int(input("a= "))  
b = int(input("b= "))      
print("Số lớn nhất là: ",so_sanh(a,b))



def xin_chao(name):
    return "Xin chào" + name

name = input("Nhap ten: ")
print(xin_chao(name))