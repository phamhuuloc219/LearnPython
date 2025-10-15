file = input("Nhập tên file: ").lower()
file_list = file.split(".")
image = ['png', 'jpg', 'jpeg', 'gif']
application = ['pdf', 'txt', 'zip']

# dog.gif
['dog', 'gif']

if file_list[1] in image:
    print(f"image/{file_list[1]}")
elif file_list[1] in application:
    print(f"application/{file_list[1]}")
else:
    print("application/octet-stream")