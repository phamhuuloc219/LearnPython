# 1. Viết chương trình yêu cầu người dùng nhập một chuỗi 
# và in ra độ dài của chuỗi đó.

# 2. Nhập một chuỗi và một ký tự, đếm số lần ký tự đó xuất hiện
# trong chuỗi.
str = input("nhập vào 1 chuỗi: ")
char = input("Nhập vào kí tự muốn đếm trong chuỗi: ")

result = str.count(char)

print("trong chuỗi",str," có",result," kí tự",char)