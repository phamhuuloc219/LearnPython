chuoi = input("Nhạp chuỗi: ")
chuoi_moi = chuoi.split(" ")
tu_dai_nhat = chuoi_moi[0]

# chuoi_moi = ['python', 'is', 'programming', 'top', '1', 'in', 'the', 'world']
for tu in chuoi_moi:
    if len(tu) > len(tu_dai_nhat):
        tu_dai_nhat = tu
        
print("từ dài nhất trong chuỗi là: ", tu_dai_nhat)
