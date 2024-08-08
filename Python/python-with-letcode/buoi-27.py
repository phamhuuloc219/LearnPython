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
    # Lặp qua từng phần tử của mảng
    for i in range(n):
        # Thiết lập một cờ để theo dõi việc hoán đổi
        swapped = False
        # Lặp qua các phần tử chưa được sắp xếp
        for j in range(0, n - i - 1):
            # So sánh các phần tử liên tiếp
            if arr[j] > arr[j + 1]:
                # Hoán đổi nếu chúng không đúng thứ tự
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Nếu không có hoán đổi nào xảy ra, thoát khỏi vòng lặp
        if not swapped:
            break

# Mảng cần sắp xếp
# arr = [64, 34, 25, 12, 22, 11, 90]
n = int(input("Nhập n= "))
arr=[]
for i in range (n):
    arr.append(int(input(f"Nhập phần tử thứ {i+1}= ")))
# Gọi hàm sắp xếp
bubble_sort(arr)

# In mảng đã được sắp xếp
print("Mảng đã được sắp xếp là:")
print(arr)