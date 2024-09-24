expresstion = input("Enter the expression: ")
x, y, z = expresstion.split(" ")
if y == "+":
    print(f"{x} {y} {z} = {int(x) + int(z)}")
elif y == "-":
    print(f"{x} {y} {z} = {int(x) - int(z)}")
elif y == "*":
    print(f"{x} {y} {z} = {int(x) * int(z)}")
elif y == "/":
    if int(z) != 0:
        print(f"{x} {y} {z} = {int(x) / int(z)}")
    else:
        print("Error: Division by zero is not allowed.")