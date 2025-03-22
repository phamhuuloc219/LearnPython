def filter_number(list):
    result = []
    for i in range(len(list)):
        if i>=0:
            result.append(i)
    return result

n = int(input("Nhập số lượng phần tử của danh sách: "))
arr = []
for i in range(n):
    number = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(number)

print("Danh sách sau khi xóa số âm:",filter_number(arr))