# Nhập số lượng phần tử của mảng
n = int(input("Nhập số lượng phần tử của mảng: "))
# Tạo 1 mảng rỗng
arr = []
# Nhập giá trị của từng phần tử vào mảng
for i in range(n):
    a = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(a)
# In ra mảng vừa nhập
print("Mảng vừa nhập là: ",arr)
# Tính bình phương từng phần tử trong mảng
for i in range(len(arr)):
    arr[i] = pow(arr[i],2)
# In ra mảng sau khi bình phương
print("Mảng sau khi bình phương: ",arr)