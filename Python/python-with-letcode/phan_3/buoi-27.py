# # Bài tập 2: in ra các số từ 1 đến n theo thứ tự ngược lại
# n = int(input("Nhập n: "))
# for i in range (n):
#     print(f"{n-i}")

# # Bài 5: In ra các số từ 1 đến 20, Nhưng bỏ qua các số chia hết cho 3
# for i in range(20):
#     if i % 3 != 0:
#         print(i)

# n = int(input("Nhập n= "))
# arr=[]
# for i in range (n):
#     arr.append(int(input(f"Nhập phần tử thứ {i+1}= ")))
# min = arr[0]
# for i in range(len(arr)):
#     if(arr[i]<min):
#         min = arr[i]
# print(min)

# n = int(input("Nhập số phần tử của dãy Fibonaci: "))
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(2,n):
#     c = a+b
#     print(c)
#     a = b
#     b = c

def bubble_sort(arr):
    n = len(arr)
    for i in range(n): # i=0
        swapped = False
        for j in range(0, n - i - 1): # 0 -> 7-1-1=5
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] = arr[j]
                swapped = True
        if not swapped:
            break

# Mảng cần sắp xếp
arr = [64, 34, 25, 12, 22, 11, 90]
# i=0
# |lan 1| 34, 64, 25, 12, 22, 11, 90 -> j=0
# |lan 2| 34, 25, 64, 12, 22, 11, 90 -> j=1
# |lan 3| 34, 25, 12, 64, 22, 11, 90 -> j=2
# |lan 4| 34, 25, 12, 22, 64, 11, 90 -> j=3
# |lan 5| 34, 25, 12, 22, 11, 64, 90 -> j=4
# |lan 6| 34, 25, 12, 22, 11, 64, 90 -> j=5
# i = 1

n = int(input("Nhập n= "))
arr=[]
for i in range (n):
    arr.append(int(input(f"Nhập phần tử thứ {i+1}= ")))
# Gọi hàm sắp xếp
bubble_sort(arr)

# In mảng đã được sắp xếp
print("Mảng đã được sắp xếp là:")
print(arr)

# danh_sach = [1,2,1,1,4,4,6,3,6,7,5]
# tap_hop= set(danh_sach)
# print(tap_hop)
# danh_sach_new = list(tap_hop)
# print(danh_sach_new)