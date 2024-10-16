import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        if sys.argv[2] in fonts:
            font = sys.argv[2]
        else:
            sys.exit("Invalid font name")
    else:
        sys.exit("Invalid usage")

    figlet.setFont(font=font)

    text = input("Text: ")

    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
