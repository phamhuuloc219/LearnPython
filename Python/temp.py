# #Slide 2
# birth_year=int(input("Enter your birth year: "))
# current_year=2024
# age=current_year-birth_year
# print("Current age: ", age)

# #Slide 3
# length_rec=int(input("Enter your length rectangle: "))
# width_rec=int(input("Enter your width rectangle: "))
# for i in range (length_rec) :
#     for j in range (width_rec) :
#         print("*",end="")
#     print()

# #Slide 4
# count=0
# sentence="Hello, I'm PHL, a student at NTU. Today, I learning Python. I'm fine"
# check=str(input("Enter a word: "))
# sentence_chuyen=sentence.split()
# for i in sentence_chuyen :
#     if(i==check):
#         count+=1
# print(count)

# def tinh_giai_thua(n):
#     giai_thua = 1
#     if n == 0:
#         return 1
#     else:
#         for i in range(1, n + 1):
#             giai_thua *= i
#         return giai_thua
# n = int(input(""))
# kq = tinh_giai_thua(n)
# print(kq)

# def tim_phep_hop(A, m, B, n):
#     i = 0
#     j = 0
#     prev_a = -1
#     prev_b = -1

#     print("", end="")

#     while i < m and j < n:
#         if A[i] < B[j]:
#             if A[i] != prev_a:
#                 print(A[i], end=" ")
#                 prev_a = A[i]
#             i += 1
#         elif B[j] < A[i]:
#             if B[j] != prev_b:
#                 print(B[j], end=" ")
#                 prev_b = B[j]
#             j += 1
#         else:
#             if A[i] != prev_a:
#                 print(A[i], end=" ")
#                 prev_a = A[i]
#             i += 1
#             j += 1

#     while i < m:
#         if A[i] != prev_a:
#             print(A[i], end=" ")
#             prev_a = A[i]
#         i += 1

#     while j < n:
#         if B[j] != prev_b:
#             print(B[j], end=" ")
#             prev_b = B[j]
#         j += 1

#     print()


# line = input().split()
# m = int(line[0])
# A = [int(x) for x in line[1:]]
# line = input().split()
# n = int(line[0])
# B = [int(x) for x in line[1:]]

# A.sort()
# B.sort()
# tim_phep_hop(A, m, B, n)

# def sap_xep(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# def Giao(setA, setB):
#     result = []
#     for element in setA:
#         if element in setB:
#             result.append(element)

#     if result:
#         result.sort()
#         for item in result:
#             print(item, end=' ')
#     else:
#         print("none")


# sizeA = int(input())
# setA = list(map(int, input().split()))

# sizeB = int(input())
# setB = list(map(int, input().split()))

# Giao(setA, setB)


# def sap_xep(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# def Giao(setA, setB):
#     result = []
#     for element in setA:
#         if element in setB:
#             result.append(element)

#     if result:
#         result.sort()
#         for item in result:
#             print(item, end=' ')
#     else:
#         print("none")

# def tim_phep_hop(A, B):
#     i = 0
#     j = 0
#     prev_a = -1
#     prev_b = -1
#     hop = []

#     while i < len(A) and j < len(B):
#         if A[i] < B[j]:
#             if A[i] != prev_a:
#                 hop.append(A[i])
#                 prev_a = A[i]
#             i += 1
#         elif B[j] < A[i]:
#             if B[j] != prev_b:
#                 hop.append(B[j])
#                 prev_b = B[j]
#             j += 1
#         else:
#             if A[i] != prev_a:
#                 hop.append(A[i])
#                 prev_a = A[i]
#             i += 1
#             j += 1

#     while i < len(A):
#         if A[i] != prev_a:
#             hop.append(A[i])
#             prev_a = A[i]
#         i += 1

#     while j < len(B):
#         if B[j] != prev_b:
#             hop.append(B[j])
#             prev_b = B[j]
#         j += 1

#     return hop

# line = input().split()
# m = int(line[0])
# A = [int(x) for x in line[1:]]

# line = input().split()
# n = int(line[0])
# B = [int(x) for x in line[1:]]

# sap_xep(A)
# sap_xep(B)

# Giao(A, B) 
# print()
# hop_result = tim_phep_hop(A, B)
# print(*hop_result)

# def sapXep(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# def timGiao(setA, setB):
#     result = []
#     for element in setA:
#         if element in setB:
#             result.append(element)

#     if result:
#         result.sort()
#         print(*result, end=' ')
#     else:
#         print("none")

# def timHop(A, B):
#     i = 0
#     j = 0
#     prev_a = -1
#     prev_b = -1
#     union_result = []

#     while i < len(A) and j < len(B):
#         if A[i] < B[j]:
#             if A[i] != prev_a:
#                 union_result.append(A[i])
#                 prev_a = A[i]
#             i += 1
#         elif B[j] < A[i]:
#             if B[j] != prev_b:
#                 union_result.append(B[j])
#                 prev_b = B[j]
#             j += 1
#         else:
#             if A[i] != prev_a:
#                 union_result.append(A[i])
#                 prev_a = A[i]
#             i += 1
#             j += 1

#     while i < len(A):
#         if A[i] != prev_a:
#             union_result.append(A[i])
#             prev_a = A[i]
#         i += 1

#     while j < len(B):
#         if B[j] != prev_b:
#             union_result.append(B[j])
#             prev_b = B[j]
#         j += 1

#     return union_result


# line = input().split()
# m = int(line[0])
# A = [int(x) for x in line[1:]]

# line = input().split()
# n = int(line[0])
# B = [int(x) for x in line[1:]]


# sapXep(A)
# sapXep(B)


# timGiao(A, B)
# print()

# kqHop = timHop(A, B)
# print(*kqHop)

# def calculate_set_difference(A, B):
#     return sorted(list(set(A) - set(B)))

# def main():
#     A_input = input("").split()
#     B_input = input("").split()

#     A = [int(x) if x.isdigit() else x for x in A_input]
#     B = [int(x) if x.isdigit() else x for x in B_input]

#     difference = calculate_set_difference(A, B)

#     if len(difference) == 0:
#         print("None")
#     else:
#         print(" ".join(str(x) for x in difference))


# main()

# def calculate_set_difference(A, B):
#     difference = []
#     for element in A:
#         if element not in B:
#             difference.append(element)
#     return sorted(difference)


# def hieuAB():
#     A_input = input("")
#     A_input = A_input.split()
#     A_count = int(A_input[0])
#     A_elements = [int(x) if x.isdigit() else x for x in A_input[1:]]

#     B_input = input("")
#     B_input = B_input.split()
#     B_count = int(B_input[0])
#     B_elements = [int(x) if x.isdigit() else x for x in B_input[1:]]

#     # Tính hiệu của hai tập hợp A và B
#     difference = calculate_set_difference(A_elements, B_elements)

#     # In kết quả
#     if len(difference) == 0:
#         print("None")
#     else:
#         difference_str = [str(x) for x in difference]
#         difference_output = " ".join(difference_str)
#         print(difference_output)
# hieuAB()

#Bài 2
# st_1 = int(input("Nhập số thứ nhất: "))
# st_2 = int(input("Nhập số thứ hai: "))
# st_3 = int(input("Nhập số thứ ba: "))
# if (st_1>st_2 and st_2>st_3 or st_3>st_2 and st_2>st_1):
#     print(st_2)
# elif (st_2>st_1 and st_1>st_3 or st_3>st_1 and st_1>st_2):
#     print(st_1)
# elif (st_2>st_3 and st_3>st_1 or st_1>st_3 and st_3>st_2):
#     print(st_3)
# else:
#     print("Số nhập không hợp lệ")

# t = 0

# for i in range(1, 101):
#     if(i % 3 == 0 and i % 5 == 0):
#         t = t + i

# print(t)
# isinstance
# k = 1
# while k <= 10:
#     print(k)
#     k += 1
# print("===============")
# l= 10
# while l >= 1:
#     print(l)
#     l -= 1
# print("===============")
# j = 1
# tong = 0
# while j <= 100 :
#     tong = tong + j
#     j += 1
# print(f"Tong la: {tong}")
# print("===============")
# n = int(input("Nhập số nguyên dương n: "))
# tong_duong = 0

# while n > 0:
#     temp = n % 10
#     tong_duong += temp
#     n //= 10

# print("Tổng các chữ số của", n, "là", tong_duong)

# print("===============")

# n = int(input("Nhập số nguyên n: "))
# so_dao_nguoc = 0

# while n > 0:
#     number = n % 10
#     so_dao_nguoc = (so_dao_nguoc * 10) + number
#     n //= 10

# print("Số đảo ngược của", n, "là", so_dao_nguoc)

# a = 10 
# bi_mat = int(input("Nhap mot so: "))
# while bi_mat != a:
#     if bi_mat < a :
#         print("so nhap nho hon so bi mat")
#     elif bi_mat > a:
#         print("so nhap lon hon so bi mat")
#     bi_mat = int(input("Nhap mot so: "))
# else:
#         print("yes")

# n = int(input("Nhập một số nguyên dương: "))
# while n <= 0:
#     print("Số nhập phải lớn hơn 0 ! Vui lòng nhập lại.")
#     n = int(input("Nhập một số nguyên dương: "))

# is_prime = True

# if n <= 1:
#     is_prime = False
# else:
#     i = 2
#     while i <= int(n**0.5):
#         if n % i == 0:
#             is_prime = False
#             break
#         i += 1

# if is_prime:
#     print(n, "là số nguyên tố")
# else:
#     print(n, "không là số nguyên tố")

# for x in range(1,5,1.5):
#     print(x)

# # so hoan hao
# def kiemtraHoanHao(n):
#     tong = 0
#     for i in range(1, n):
#         if (n % i) == 0:
#             tong += i
#     if tong == n:
#         return True
#     else:
#         return False


# n = int(input('Nhap vao so nguyen n lon hon 0: '))
# while n<0:
#     n = int(input('Nhap vao so nguyen n lon hon 0: '))
# if kiemtraHoanHao(n):
#     print(n, ' la so hoan hao')
# else:
#     print(n, ' khong la so hoan hao')
    
# # fibonaci
# def fibonacci(n):
#     f0 = 0
#     f1 = 1
#     fn = 1
 
#     if (n < 0):
#         return -1
#     elif (n == 0 or n == 1):
#         return n
#     else:
#         for i in range(2, n):
#             f0 = f1
#             f1 = fn
#             fn = f0 + f1
#         return fn
    
# n = int(input("Nhap so phan tu cua day fibonaci: "))
# print(f"{n} số đầu tiên của dãy số fibonacci: ")

# sb = ""
# for i in range(0, n):
#     sb = sb + str(fibonacci(i)) + ", "
# print(sb)

# f0 = 0
# f1 = 1
# n = int(input("Nhap so phan tu trong day fibo: "))

# print(f"{f0} {f1} ", end="")
# for i in range (1,n):
#     fn = f0 + f1
#     print(fn,end=" ")
#     f0 = f1
#     f1 = fn





# def t_ong(n):
#     tong = 0
#     for i in range (1,n+1):
#         tong = tong + i
#     return tong
# n = int(input("nhập số nguyên: "))

# print ('tổng từ 1 đến', n,'là',t_ong(n))

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# # Ví dụ kiểm tra
# number = 2
# if is_prime(number):
#     print(f"{number} là số nguyên tố")
# else:
#     print(f"{number} không phải là số nguyên tố")
 

# n = 10
# for i in range (n,0,-1):
#     print(i)

# from tkinter import *
# from tkinter.font import Font
# wd=Tk()
# wd.geometry('320x320')
# wd.title('Máy tính')
# fts=Font(family='Tohoma',size=12)
# drnum=8
# py=5
# mh=Label(wd,bg='#c5cacd',fg='#FFFFFF',width=320,height=3,font=fts)
# mh.pack(side=TOP)
# fr=Frame(wd)
# fr.pack()
# #HAM TAO BIEU THUC DANG CHUOI
# bieuthuc=''
# def xyly(num):
#     global bieuthuc
#     bieuthuc=bieuthuc+str(num)
#     mh.config(text=bieuthuc)

# def TinhToan():
#     global ketqua
#     global bieuthuc
#     ketqua=eval(bieuthuc)
#     mh.config(text=ketqua)
#     bieuthuc=''
# def Xoa():
#     global bieuthuc
#     mh.config(text='')
#     bieuthuc=''
#     print(bieuthuc)

# #HANG 1
# bt7=Button(fr,text='7',font=fts,width=drnum,pady=py,command=lambda:xyly('7'))
# bt7.grid(row=1,column=1)
# bt8=Button(fr,text='8',font=fts,width=drnum,pady=py,command=lambda:xyly('8'))
# bt8.grid(row=1,column=2)
# bt9=Button(fr,text='9',font=fts,width=drnum,pady=py,command=lambda:xyly('9'))
# bt9.grid(row=1,column=3)
# btCong=Button(fr,text='+',font=fts,width=drnum,pady=py,command=lambda:xyly('+'))
# btCong.grid(row=1,column=4)
# #HANG 2
# bt4=Button(fr,text='4',font=fts,width=drnum,pady=py,command=lambda:xyly('4'))
# bt4.grid(row=2,column=1)
# bt5=Button(fr,text='5',font=fts,width=drnum,pady=py,command=lambda:xyly('5'))
# bt5.grid(row=2,column=2)
# bt6=Button(fr,text='6',font=fts,width=drnum,pady=py,command=lambda:xyly('6'))
# bt6.grid(row=2,column=3)
# btTru=Button(fr,text='-',font=fts,width=drnum,pady=py,command=lambda:xyly('-'))
# btTru.grid(row=2,column=4)
# #HANG 3
# bt1=Button(fr,text='1',font=fts,width=drnum,pady=py,command=lambda:xyly('1'))
# bt1.grid(row=3,column=1)
# bt2=Button(fr,text='2',font=fts,width=drnum,pady=py,command=lambda:xyly('2'))
# bt2.grid(row=3,column=2)
# bt3=Button(fr,text='3',font=fts,width=drnum,pady=py,command=lambda:xyly('3'))
# bt3.grid(row=3,column=3)
# btNhan=Button(fr,text='*',font=fts,width=drnum,pady=py,command=lambda:xyly('*'))
# btNhan.grid(row=3,column=4)
# #HANG 4
# btDel=Button(fr,text='Del',font=fts,width=drnum,pady=py,command=Xoa)
# btDel.grid(row=4,column=1)
# bt0=Button(fr,text='0',font=fts,width=drnum,pady=py,command=lambda:xyly('0'))
# bt0.grid(row=4,column=2)
# btChia=Button(fr,text='/',font=fts,width=drnum,pady=py,command=lambda:xyly('/'))
# btChia.grid(row=4,column=3)
# btBang=Button(fr,text='=',font=fts,width=drnum,pady=py,command=TinhToan)
# btBang.grid(row=4,column=4)
# wd.mainloop()

# a = (input("a= "))
# while len(a)>0:
#     if a == a[::-1]:
#         print("So nay la so doi xung")
#         break
#     else:
#         print("so nay la so khong doi xung")
#         break
# num = 6
# if num < 4:
#     print("yes")
# elif num <5:
#     print("yesssss") 
# else:
#     print("no")

def them_sinh_vien(list):
    while True:
        name = input("Nhập tên sinh viên: ")
        
        stripped_name = name.strip()
        if stripped_name != "":
            valid_name = True
            for c in name:
                if not (c.isalpha() or c.isspace()):
                    valid_name = False
                    break
            if valid_name:
                break
        print("Vui lòng nhập lại tên hợp lệ")
    
    while True:
        ID = input("Nhập mã số sinh viên: ")
        
        if ID.isdigit():
            if len(ID) >= 3:
                break
        print("Vui lòng nhập lại mã sinh viên hợp lệ")
    
    while True:
        diem = input("Nhập điểm sinh viên: ")
        
        is_valid_score = True
        parts = diem.split('.')
        if len(parts) <= 2:
            for part in parts:
                if not part.isdigit():
                    is_valid_score = False
                    break
            if is_valid_score:
                if 0 <= float(diem) <= 10:
                    break
        print("Vui lòng nhập lại điểm hợp lệ")
    
    list.append({'tên': name, 'mã số': ID, 'điểm': float(diem)})

dssv = []
while True:
    print("1. Thêm sinh viên")
    print("2. Thoát")
    
    choice = input("Chọn chức năng (1/2): ")
    
    if choice == '1':
        them_sinh_vien(dssv)
        print("Thêm sinh viên thành công")
    elif choice == '2':
        print("Xin chào và chúc bạn học tập tốt! ")
        print(dssv)
        break
    else:
        print("Chức năng khằng hợp lệ")

