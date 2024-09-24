images = ["jpg", "gif", "jpeg", "png"]
application = [ "pdf", "txt", "zip"]
def extentions(file):
    file = file.split(".")
    if file[1] in images:
        return f"image/{file[1]}"
    elif file[1] in application:
        return f"application/{file[1]}"
    else:
        return "application/octet-stream"
def main():
    file = input("Enter a file name: ")
    print(extentions(file))
if __name__ == "__main__":
    main()

# file = "hello.jpg"
# file = file.split(".")
# if file[1] in images:
#     print(f"image/{file[1]}")
# else: 
#     print("hello")