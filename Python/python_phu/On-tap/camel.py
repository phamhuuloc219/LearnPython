text = input("nhập vào tên của một biến ở dạng camelCase: ")
result = ""
for i in range(len(text)):
    if text[i].isupper():
        result += "_"
        result += text[i].lower()
    else:
        result += text[i]
        
print(result)