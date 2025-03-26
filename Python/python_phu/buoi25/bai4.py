# Nhập số lượng phần tử của mảng
n = int(input("Nhập số lượng phần tử của mảng: "))
# Tạo 1 mảng rỗng
arr = []
# Nhập giá trị của từng phần tử vào mảng
for i in range(n):
    a = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(a)
    
# Cách 1:
SLN = arr[0]
for i in range(len(arr)):
    if arr[i] > SLN:
        SLN = arr[i]
        
print("SLN:", SLN)

SNN = arr[0]
for i in range(len(arr)):
    if arr[i] < SNN:
        SNN = arr[i]
        
print("SNN:", SNN)
# Cách 2:
# print("SLN: ",max(arr))  
# print("SNN: ",min(arr))   
 