# ten = input("Nhap ten:")

for i in range(1,11): # in ra màn hình 1-10
   print(i)
   
number_1 = int(input("Nhap so= "))
# Nếu nhập 1 số <0 thì nhập lại cho đến khi nào >0 thì dừng
while number_1<0: # nếu điều kiện đúng => thực hiện
    print("Vui lòng nhập 1 số >0")
    number_1 = int(input("Nhập lại:"))
    
print("số bạn vừa nhập :", number_1)



# Cấu trúc rẽ nhánh
# if <Điều kiện1>:
#     <Khối lệnh trong if>
# elif <Điều kiện2>:
#     <Khối lệnh trong elif>
# else: #Ngược lại với tất cả các trường hợp liệt kê ở treen

# Vòng lặp for: vòng lặp với số lần biết trước
# for <Biến lặp> in <chuỗi lặp>:
#     <Khối lệnh trong for>
# Vòng lặp while: vòng lặp có điều kiện



a= 5
b = 20
for i in range(a,b+1):
    if(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0 and i%5==0):
        print("Fizz Buzz")
    else:
        print(i)