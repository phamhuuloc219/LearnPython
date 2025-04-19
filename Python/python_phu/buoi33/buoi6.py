n = int(input("Nhập số lượng phần tử: "))
arr = []
for i in range(1,n+1):
    arr.append(int(input(f"Nhập phần tử thứ {i}: ")))
print("Danh sách vừa nhập:", arr)

tong = 0
for i in range(len(arr)):
    tong = tong + arr[i]
tbc = tong / n
print("Trung bình cộng của danh sách là:", round(tbc,2))