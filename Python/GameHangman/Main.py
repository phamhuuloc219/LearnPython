import pygame
import random
import os

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Thiết lập màn hình game
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

images = [pygame.image.load(f'D:/Learning/GitHub/LearnPython/Python/GameHangman/images/hang{i}.png') for i in range(12)]

hangman_status = 0
words = ['PYTHON', 'PYGAME', 'CODING', 'HANGMAN']
word = random.choice(words)
guessed = []
FPS = 60
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 40)

# Vẽ từ và các chữ cái đoán
def draw():
    win.fill(WHITE)

    # Vẽ từ đã đoán
    display_word = ''
    for letter in word:
        if letter in guessed:
            display_word += letter + ' '
        else:
            display_word += '_ '
    text = font.render(display_word, True, BLACK)
    win.blit(text, (400, 200))

    # Vẽ trạng thái Hangman
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

# Xử lý đoán chữ cái
def check_guess(guess):
    global hangman_status
    if guess not in word:
        hangman_status += 1
    guessed.append(guess)

run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            guess = chr(event.key).upper()
            if guess.isalpha() and guess not in guessed:
                check_guess(guess)

    draw()

    if hangman_status == 11:
        print("You Lost!")
        run = False

    if all(letter in guessed for letter in word):
        print("You Won!")
        run = False

pygame.quit()