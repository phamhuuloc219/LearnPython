n = int(input("Nhập n= "))
dem = 0
for i in range(1, n+1):
    if i % 3 == 0:
        dem +=1
print("Các số chia hết cho 3 từ 1 đến",n,"là: ", dem)    