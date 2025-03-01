# def is_camelCase(cc):
#     b = 0
#     while b < len(cc):
#         if b == 0:
#             if not cc[b].islower():
#                 return False
#         elif cc[b].isupper():
#             if cc[b-1].isupper():
#                 return False
#         b += 1
#     return True

# def snake_case(a):
#     new_string = ""
#     for i in a:
#         if i.isupper():
#             new_string += "_" + i.lower()
#         else:
#             new_string += i
#     return new_string

# a = input("Input camelCase: ")
# while is_camelCase(a) == False or not isinstance(a, str):
#     a = input("Input *camelCase*: ")
# results = snake_case(a)
# print(f"snake_case: {results}")

# File: camel.py

camel_case = input("Nhập tên biến ở dạng camelCase: ")

snake_case = ""

for ky_tu in camel_case:
    if ky_tu.isupper():
        snake_case += "_" + ky_tu.lower()
    else:
        snake_case += ky_tu

print("Tên biến ở dạng snake_case:", snake_case)