def find_repairs(list, k):
    result = []
    for i in range(len(list)):
        for j in range(i +1, len(list)):
            if list[i] + list[j] == k:
                result.append([list[i], list[j]])
    return result

arr = [3, 7, 1, 20, 9]
k = int(input("Nhap k: "))
print("Các cặp số có tổng bằng ",k," là: ",find_repairs(arr, k))