import random

def main():
    level = get_level()
    score = 0

    for i in range(10):  # Tạo 10 bài toán
        X = generate_integer(level)
        Y = generate_integer(level)
        correct_answer = X + Y
        attempts = 0

        while attempts < 3:  # Tối đa 3 lần thử
            try:
                answer = int(input(f"{X} + {Y} = "))
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        if attempts == 3:
            print(f"Câu trả lời đúng là: {correct_answer}")

    print(f"Điểm của bạn: {score}/10")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass  # Bỏ qua và yêu cầu người dùng nhập lại

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level không hợp lệ!")

if __name__ == "__main__":
    main()
