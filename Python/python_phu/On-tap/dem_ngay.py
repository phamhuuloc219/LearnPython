a = int(input("Nhập số bi hiện có: ")) 
b = int(input("Nhập số bi mong muốn đạt được: "))
ngay_du_kien = b//2
if(a>=b):
    print("0 ngày")
else:
    for i in range(1, ngay_du_kien +1):
        a += 2
        if (a >= b):
            print("Số ngày để đạt được B viên bi là: ",i)
            break