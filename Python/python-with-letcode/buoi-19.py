tho_ho_xuan_huong = """Thân em thời trắng phận em tròn,
Bảy nổi ba chìm mấy nước non.
Rắn nát mặc dầu tay kẻ nặn,
Mà em vẫn giữ tấm lòng son."""

print("Bai tho co: ",len(tho_ho_xuan_huong)," ki tu")

dau = tho_ho_xuan_huong.find("nước non")
cuoi = dau + len("nước non")
trich = tho_ho_xuan_huong[dau:cuoi]
print(trich)

lines = tho_ho_xuan_huong.strip().split('\n')
for line in lines[:2]:
    print(line)


print(tho_ho_xuan_huong[-1])

for line in lines[2:]:
    print(line)