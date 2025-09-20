name = 'Loc'
age = 23
gender = True # True là nam, False là nữ
height = 1.7
# kiểm tra kiểu dữ liệu của biến
print("Kiểu dữ liệu của name: ",type(name)) 
print("Kiểu dữ liệu của gender: ",type(gender))
print("Kiểu dữ liệu của age: ",type(age))
print("Kiểu dữ liệu của height: ",type(height))

a = 21
b = 9
ket_qua_cong = a + b
ket_qua_tru = b - a
...
print("Kết quả của phép cộng", a, "+", b, "=", ket_qua_cong)
print("Kết quả của phép trừ", b, "-", a, "=", ket_qua_tru)
# chia lấy dư
ket_qua = a % b
print("Kết quả của phép chia lấy dư: ",ket_qua)
# Biến có thể thay đổi trong quá trình chương trình thực hiện
ket_qua = a // b
print("Kết quả của phép chia lấy nguyên: ",ket_qua)