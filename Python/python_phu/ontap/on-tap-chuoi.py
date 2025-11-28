n = "Welcome to Da Lat city"   
print("a:",n[11:16+1])
print("b:",n[8:21+1])
print("c:",n.lower())
print("d:",n.replace("Da Lat","Đà Lạt"))

e = n.split(" ") # danh sách sau khi tách
for m in e:
    if m == 'to':
        print("Đi Đà Lạt thôi")
        break
    # else:
    #     print(m)