# #Start code here
# import random
# secret_number = int(random.randrange(0, 100))
# number = int(input("Nhập vào 1 số bất kỳ"))
# while secret_number != number:
#   if secret_number - 3 <= number and secret_number + 3 >= number:
#     print("số người dùng nhập vào gần với số bí mật")
#     number = int(input("Nhập lại: "))
#   elif secret_number > number:
#     print("số người dùng nhập vào lớn hơn số bí mật")
#     number = int(input("Nhập lại: "))
#   elif secret_number < number:
#     print("số người dùng nhập vào lớn hơn số bí mật")
#     number = int(input("Nhập lại: "))
# print("chúc mừng")


# string_b = """Nevertheless, his character is an interesting one, and well repays study. Throughout the calculated extravagance of his adventures, d’Eon’s indomitable energy persists, and the scandal caused by his conduct a century and a half ago should not blind us to his genuine services. There is a sustained interest in following d’Eon into many countries from Russia to England, and into many surroundings from the court of the Empress Elizabeth or the camp of Marshal de Broglie to the palace of Versailles and the shops of London, wherever, in fact, the Chevalier’s adventures led him for a period of more than sixty years; at one time as a diplomatist, again[19] as a dragoon, or, as Latour represents him in one of his charming pastels, as a woman."""
# abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
# # dem_ki_tu_a = string_b.count("a")
# # dem_ki_tu_i = string_b.count("i")

# # print("Số lượng ký tự a có trong chuỗi là:", dem_ki_tu_a)
# # print("Số lượng ký tự i có trong chuỗi là:", dem_ki_tu_i)
# dem_ki_tu_a = 0
# dem_ki_tu_i = 0
# for str in abc:
#     if str == "a":
#         dem_ki_tu_a += 1
#     elif str == "i":
#         dem_ki_tu_i += 1
# print("Số lượng ký tự a có trong chuỗi là:", dem_ki_tu_a)
# print("Số lượng ký tự i có trong chuỗi là:", dem_ki_tu_i)



camel = input("Input camelCase: ")
snake = ""

for char in camel:
    if char.isupper():
        snake += "_" + char.lower()
    else:
        snake += char

print("output: ",snake)