import random

def main():
    while True:
        try:
            level = int(input("Nhập cấp độ (n): "))
            if level > 0:
                break
        except ValueError:
            pass

    secret_number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Đoán số: "))
            if guess <= 0:
                continue
            if guess < secret_number:
                print("Too small!")
            elif guess > secret_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass

if __name__ == "__main__":
    main()
