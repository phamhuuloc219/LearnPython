# fruits=["apple","mango","banana","orange","kiwi"]
# # Cú pháp
# # Giá trị trả về là một danh sách mới, giữ nguyên danh sách cũ
# # newList=[expresstion for item in iterable if condition == True]
# newList=[i for i in fruits if"a" in i]
# # Condition
# newList2=[i for i in fruits if i!="apple"] #condition là điều kiện mà phần tử phải thỏa mãn để được đưa vào danh sách mới
# newList3=[i for i in fruits] #condition là tùy chọn và có thể bỏ qua

# print("Phần tử chứa kí tự 'a' của fruits: ",newList)
# print("Danh sách chứa fruits trừ 'apple': ",newList2)
# print(newList3)
# # Interable
# newList4=[i for i in range(10) ] # iterable có thể là bất kỳ đối tượng iterable nào, như list, tuple, set,...
# print("Danh sách các phần tử chạy từ 0 đến <10: ",newList4)
# newList5=[i for i in range(10) if i<5]
# print("Danh sách các phần tử chạy từ 0 đến <5: ",newList5)
# #Expression:
# # expression là phần tử hiện tại trong quá trình lặp, 
# # nhưng nó cũng là kết quả cuối cùng, 
# # mà ta có thể thay đổi trước khi nó trở thành một phần tử danh sách trong danh sách mới.
# newList6=[i.upper() for i in fruits] #Đặt các giá trị trong danh sách mới thành chữ hoa.
# print("Đặt danh sách thành chữ hoa: ",newList6)
# newList7=['hello' for i in fruits] # Ta có thể đặt kết quả thành bất cứ thứ gì. VD đặt các giá trị trong danh sách mới thành “hello”
# print("Đặt danh sách thành tất cả là 'hello': ",newList7)
# #expression là biểu thức được áp dụng lên mỗi phần tử của danh sách cũ để tạo phần tử tương ứng trong danh sách mới
# newList8=[i if i!='banana' else 'orange' for i in fruits] #Trả về phần tử nếu nó không phải là banana, nếu là banana thì trả về orange.
# print("List sau khi đổi banana -> orange: ",newList8)

###############################################################################################################################
#Tạo một danh sách chứa các số nguyên tố từ 1 đến 50.
def check_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
listSNT=[i for i in range(1,51) if check_prime(i)]
print(listSNT)