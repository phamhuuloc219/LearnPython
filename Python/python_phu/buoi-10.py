# dem = 0
# while (dem < 3):
#     print("Hello Phú")  
#     dem += 1
# print("goodbye")

# #Bài 1: Dùng vòng lặp while in ra các số từ 1 đến 10
# n = 1
# while (n<=10):
#     print(n)
#     n += 1

# #Bài 2: Dùng vòng lặp while in ra các số từ 10 đến 1
# m = 10
# while (m >= 1):
#     print(m)
#     m -= 1
    
# #Bài 3: Dùng vòng lặp while in ra các số chẵn từ 1 đến 20
# i = 1
# while (i <= 20):
#     if(i % 2 == 0):
#         print(i)
#     i += 1
# #Bài 4: Dùng vòng lặp while in ra các số lẻ từ 1 đến 20
# n = 1
# while(n<=20):
#     if (n % 2 != 0):    
#         print(n)
#     n+=1
#Bài 5: Dùng vòng lặp while để kiểm tra mật khẩu nhập vào có phải là "Python" hay không.
# Nếu là "Python" thì in ra "Đúng mật khẩu" và thoát vòng lặp, nếu không thì in ra "Sai mật khẩu"
# và yêu cầu người dùng nhập lại mật khẩu.
password = "Python"
while True:
    passwords = input("Enter your password: ")
    if passwords == password:
        print("Đúng mật khẩu")
        break # Dừng lại vòng lặp
    else:
        print("Sai mật khẩu. Vui lòng nhập lại.")
print("Goodbye")
print("Goodbye")
print("Goodbye")
print("Goodbye")
print("Goodbye")