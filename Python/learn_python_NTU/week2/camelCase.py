def is_camelCase(cc):
    b = 0
    while b < len(cc):
        if b == 0:
            if not cc[b].islower():
                return False
        elif cc[b].isupper():
            if cc[b-1].isupper():
                return False
        b += 1
    return True

def snake_case(a):
    new_string = ""
    for i in a:
        if i.isupper():
            new_string += "_" + i.lower()
        else:
            new_string += i
    return new_string

a = input("Input camelCase: ")
while is_camelCase(a) == False or not isinstance(a, str):
    a = input("Input *camelCase*: ")
results = snake_case(a)
print(f"snake_case: {results}")