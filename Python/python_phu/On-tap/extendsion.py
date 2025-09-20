application = ["doc", "docx", "pdf", "xlsx"]
image = ["png", "jpg", "jpeg", "gif"]
video = ["mp4" , "mov" , "mkv"]

file = input("Nhập tên file: ").lower() # dog.pitbull.mp3.png.mp4

# tách chuỗi thành danh sách 
file_list = file.split(".") # ví dụ ['dog', 'pitbull', 'mp3', 'png', 'mp4']

file_tail = file_list[-1] # Đuôi file

if file_tail in application:
    print(f"application/{file_tail}")
elif file_tail in image:
    print(f"image/{file_tail}")
elif file_tail in video:
    print(f"video/{file_tail}")
else:
    print("application/octet-stream")
    