# danh_sach_trai_cay = ["apple", "orange", "kiwi", [534,342,6324.645]]

# for i in danh_sach_trai_cay:
#     print(i)
    
# print("Đã in xong kết quả")
    
    
    
# # Tính tổng các số trong danh sách
# tong = 0
# list_number = [4,3,1,2,6,7,8,12,43,534,324,645,234,654,2]
# for i in list_number:
#     print("Giá trị của phần tử ở lần lặp này là:",i)
#     tong = tong + i
#     print("Tổng các số trong lần lặp này là:",tong)
#     print("================================================")
# # print("Tổng các số trong danh sách là: ", tong)

list = ["Code", "python", "is", "fun", "and", "stress"]
for i in list:
    if i == "and": # nếu gặp phần tử and sẽ dừng vòng lặp
        break
    else: # nếu không gặp phần tử and thì sẽ in ra màn hình
        print(i,end=' ') # end = '' in thẳng hàng
