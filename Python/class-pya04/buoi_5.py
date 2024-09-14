a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
pt = input("Nhập phép tính: ")
ket_qua = 0
if (pt == "+"):
    ket_qua = a + b
elif (pt == "-"):
    ket_qua = a - b
elif (pt == "x"):
    ket_qua = a * b
elif (pt == "/"):
    if(b != 0):
        ket_qua = a / b
    else:
        print("khong chia duoc")
else:
    print("phép tính không hợp lệ!!!")

print("kết quả = ",ket_qua)