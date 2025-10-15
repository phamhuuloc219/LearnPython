# Bài 1: Viết một chương trình để đảo ngược thứ tự của một danh sách

# Bài 2: Viết chương trình loại bỏ các phần tử trùng lặp trong một
#  danh sách
# n = int(input("Nhập số lượng phần tử: "))
# arr = []
# for i in range(n):
#     arr.append(int(input("Nhập phần tử: ")))
# print("Danh sách vừa nhập:", arr)
    
# result =[]    
# for i in range(len(arr)):
#     if arr[i] not in result:
# 	    result.append(arr[i])
     
# print("Danh sách sau khi loại bỏ phần tử trùng lặp:",result)

# Bài 3: Viết chương trình tìm phần tử lớn nhất và phần tử nhỏ nhất
#  trong danh sách


# Bài 4: Viết chương trình tính tổng các phần tử lớn hơn 0
# - Nhập số lượng phần tử
# - Nhập giá trị của phần tử
# - Duyệt qua vòng lặp For
# + Nếu giá trị phần tử > 0 thì mình sẽ + vào cái tổng
# - IN ra Tong

# Bài 5: Viết chương trình đếm số lần xuất hiện của các phần tử
#  trong danh sách

def dem_so_lan_xuat_hien(list):
    # Lưu số lần xuất hiện của phần tử
    counts = []
    # Lưu giá trị của phần tử
    values = []
    for i in range(len(list)):
        if list[i] in values:
            index = values.index(list[i])
            counts[index] += 1
        else:
            values.append(list[i])
            counts.append(1)
    
    for i in range(len(values)):
        print(f"Phần tử {values[i]} xuất hiện {counts[i]} lần")

n = int(input("Nhập số lượng phần tử: "))
arr = []
for i in range(n):
    arr.append(int(input("Nhập phần tử: ")))
print("Danh sách vừa nhập:", arr)

dem_so_lan_xuat_hien(arr)
