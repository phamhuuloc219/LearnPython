# empty_list=[]
# numers=[1,2,3,4,5,6,7,8,9,10]
# names=['Loc','Kiet','Thang']
# mixed_list=[1,2,'Loc',True,3.13]

# ################################################################################################################################
# print("find 3 in numbers:")
# # Cách 1: Kiểm tra theo index (vị trí của phần tử)
# # Hàm index() trả về vị trí phần tử của mảng. Nếu phần tử không tồn tại sẽ báo lỗi.
# try:
#     index=numers.index(3)
#     print("index=",index)
# except ValueError:
#     print("no")
# # Chú thích:
# # try: Đây là khối chứa mã bạn muốn thực thi. Khi các lệnh trong khối này gặp phải ngoại lệ, luồng điều khiển sẽ chuyển đến khối "except" tương ứng để xử lý lỗi.
# # except: Đây là khối chứa mã xử lý cho ngoại lệ. Bạn có thể xác định loại ngoại lệ cụ thể mà bạn muốn xử lý, hoặc bạn có thể sử dụng except mà không định rõ loại ngoại lệ (tức là xử lý mọi loại ngoại lệ).
# # Loa Ngoai Re: Là tên của loại ngoại lệ mà bạn muốn xử lý trong khối "except". Ví dụ: ValueError, TypeError, ZeroDivisionError,...

# ################################################################################################################################
# # Cách 2: Sử dụng toán tử in
# if 3 in numers:
#     print("Co")
# else:
#     print("Khong")
#  ################################################################################################################################   
# #Cách 2: Sử dụng toán tử "not in"
# if "Loc" not in names:
#     print("khong cos Loc trong names")
# else:
#     print("cos Loc trong names")
#  ################################################################################################################################   
# #Cách 3: Sử dụng phương thức count(): Đếm số lần xuất hiện của phần tử.
# count_3=numers.count(3)
# if count_3>0:
#     print(count_3," times")
# else: print("Khong ton tai")
# ################################################################################################################################
# # Trích xuất mảng con
# print(numers[:2]) # 0->1
# print(numers[0:3]) # 0->2
# print(numers[2:5]) # 2->4
# ################################################################################################################################
# print("Mảng: ",numers)
# # Xóa phần tử trong mảng thông qua toán tử del
# print("Xóa phần tử sử dụng toán tử del:")
# del numers[2]  # xoa vi tri 2
# del numers[5:9] # xoa vi tri tu 5-8
# print(numers)

# # Sử dụng phương thức Remove() (Chỉ xóa giá trị đầu tiên)
# print("Xóa phần tử sử dụng phương thức remove():")
# numers.remove(2)
# print(numers)

# # Sử dụng phương thức pop() 
# # Phương thức pop() xóa phần tử tại chỉ mục được chỉ định và trả về giá trị của phần tử đã xóa. Nếu không chỉ định chỉ mục, phương thức pop() sẽ mặc định xóa phần tử cuối cùng trong mảng.
# print("Xóa phần tử sử dụng phương thức pop():")
# deleted_value=numers.pop(2)
# print(numers)
# print("Phần tử đã xóa: ",deleted_value)

# deleted_value=numers.pop() # xóa phần tử cuối cùng
# print(numers)
# print("Phần tử đã xóa: ",deleted_value)
# ################################################################################################################################
# ################################################################################################################################
# ################################################################################################################################
# ################################################################################################################################

# arr1=[1,2,3]
# arr2=[4,5,6]
# result_arr=arr1+arr2
# print ("Nối mảng:",result_arr)

# arr1.extend(arr2)
# print("Nối mảng sử dụng phương thức extend:",arr1)

# for element in arr2:
#     arr1.append(element)
# print("Nối mảng sử dụng append:",arr1)

########################################################################################################

# # Đảo ngược mảng sử dụng phương thức reverse()
# numbers=[1,2,3,4,5]
# print("Mảng trước khi đảo ngược: ",numbers)
# numbers.reverse()
# print("Mảng sau khi đảo ngược: ",numbers)

########################################################################################################

# numbers=[1,5,2,4,3,6,8,32]
# # Sắp xếp mảng theo thứ tự tăng dần sử dụng sort()
# numbers.sort()
# print("Sắp xếp theo thứ tự tăng dần: ", numbers)
# # Sắp xếp mảng theo thứ tự giảm dần bằng cách sử dụng reverse=True
# numbers.sort(reverse=True)
# print("Sắp xếp theo thứ tự giảm dần: ", numbers)

########################################################################################################

# # Duyệt các phần tử của mảng
# numbers=[1,2,3,4,5]
# for i in range(0,len(numbers)):
#     print("Vị trí:"+str(i)+" có giá trị là:"+str(numbers[i]))

########################################################################################################

# Viết một hàm kiểm tra mảng có giảm dần hay tăng dần hay không
# Cách 1
def checkArray1(arr):
    tang=all(arr[i]<=arr[i+1] for i in range(len(arr)-1))
    giam=all(arr[i]>=arr[i+1] for i in range(len(arr)-1))
    # sử dụng hàm all để kiểm tra xem tất cả các phần tử trong một danh sách đều thoả mãn một điều kiện nào đó.
    # Hàm all trong Python trả về True nếu tất cả các phần tử trong danh sách đầu vào đều mang giá trị True. 
    # Nếu có ít nhất một phần tử trong danh sách đầu vào mang giá trị False, hoặc danh sách đầu vào là rỗng, thì hàm all sẽ trả về False.
    
    if tang:
        print("The array is in acsending order.")
    elif giam:
        print("The array is in descending order.")
    else:
        print("The array is not in ascending or descending order.")

arr1=[1,2,3,4,5]
checkArray1(arr1)
arr2=[5,4,3,3,2]
checkArray1(arr2)
arr3=[4,4,1,2,1]
checkArray1(arr3)

# Cách 2
def checkArray2(arr):
    tang=sorted(arr)==arr
    giam=sorted(arr, reverse=True)==arr
    # sử dụng hàm sorted để tạo ra một bản sao của mảng đã được sắp xếp theo thứ tự tăng dần và giảm dần. 
    # Sau đó, chúng ta so sánh mảng ban đầu với các bản sao đã sắp xếp để xác định xem mảng có được sắp xếp theo thứ tự tăng dần hay giảm dần không.
    if tang and not giam:
        print("The array is in acsending order.")
    elif giam and not tang:
        print("The array is in descending order.")
    else:
        print("The array is not in ascending or descending order.")

arr4=[4,5,6,7]
arr5=[7,6,5,4]
arr6=[3,1,4,3]
checkArray2(arr4)
checkArray2(arr5)
checkArray2(arr6)