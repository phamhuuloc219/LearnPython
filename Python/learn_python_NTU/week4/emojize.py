import emoji as e

def main():
    user = input("Enter a str with emoji code or alias: ") # :1st_place_medal:, :smile_cat:

    emoji_version = e.emojize(user,language="alias")
    print(emoji_version)

if __name__ == "__main__":
    main()
