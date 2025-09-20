while True:
    str = input().upper()
    if str == "E":
        break
    result = str.replace(" ","_")
    print("->",result)