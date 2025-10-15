# Bài 1: Lọc số chẵn và số lẻ:
# Cho danh sách số nguyên, tách riêng danh sách số chẵn và số lẻ.
# n = int(input("Nhập số lượng phần tử của danh sách: "))
# arr = []
# for i in range(n):
#     number = int(input(f"Nhập phần tử thứ {i+1}: "))
#     arr.append(number)
# print("Danh sách vừa nhập:", arr)

# so_chan = []
# so_le = []

# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         so_chan.append(arr[i])
#     else:
#         so_le.append(arr[i])

# print("Danh sách số chẵn:", so_chan)
# print("Danh sách số lẻ:", so_le)


# Bài 2: Sắp xếp danh sách:
# Viết chương trình sắp xếp danh sách theo thứ tự tăng dần mà không dùng sort().

# Bài 3: Xoá phần tử:
# Nhập một danh sách số nguyên và một số x. Xóa tất cả các phần tử có giá trị x trong danh sách.

n = int(input("Nhập số lượng phần tử của danh sách: "))
arr = []
for i in range(n):
    number = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(number)
print("Danh sách vừa nhập:", arr)
x = int(input("Nhập số x: "))

# Cách 1: xóa phần tử bằng cách thêm những phần tử khác x vào 1 danh sách khác
result = []

for i in range(len(arr)):
    if arr[i] != x:
        result.append(arr[i])
        
print("Danh sách sau khi xóa phần tử x:", result)

# Cách 2: Xóa phần tử trực tiếp

for i in range(len(arr)-1, -1 , -1):
    if arr[i] == x:
        arr.pop(i)
        
print("Danh sách sau khi xóa phần tử x:", arr)
