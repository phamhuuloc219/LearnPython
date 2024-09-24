def convert(s):
    s = s.replace(":)","🙂")
    s = s.replace(":(","😔")
    return s
def main():
    s = input("Enter the message: ")
    print(convert(s))
if __name__ == "__main__":
    main()