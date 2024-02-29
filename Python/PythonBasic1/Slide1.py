#CountDown
# import time
# print("Bắt đầu đếm ngược...")
# for i in range(5,0,-1):
#     print(i)
#     time.sleep(1)
# print("Welcome here!!!")

################################################################
#Random
#   Random number
# import random
# number=random.randint(0,10)
# print("Random number: " + str(number))
#   Random List
# Fruits=["apple", "orange", "banana","mango"]
# fruit=random.choice(Fruits)
# print("Random fruit: " + fruit)

################################################################
# import platform
# if platform.system() == "Windows":
#     print("Windows")
# elif platform.system() == "Darwin":
#     print("macOS")
# else:
#     print("Current: ",platform.system())

################################################################
import datetime
name=input("Enter your name: ")
print("Hello ",name)
print(f"Hello {name}")
print("I'm assistant")
print("Current date and time", datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))