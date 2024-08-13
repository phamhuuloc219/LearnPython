import random

def get_user_choice():
    user_choice = input("Chọn búa, bao, kéo: ").lower()
    while user_choice not in ['búa', 'bao', 'kéo']:
        print("Lựa chọn không hợp lệ. Vui lòng chọn búa, bao hoặc kéo.")
        user_choice = input("Chọn búa, bao, kéo: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['búa', 'bao', 'kéo'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Hòa!"
    elif (user_choice == 'búa' and computer_choice == 'kéo') or \
         (user_choice == 'bao' and computer_choice == 'búa') or \
         (user_choice == 'kéo' and computer_choice == 'bao'):
        return "Bạn thắng!"
    else:
        return "Máy thắng!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Bạn chọn: {user_choice}")
    print(f"Máy chọn: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

play_game()