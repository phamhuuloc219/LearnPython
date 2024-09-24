def main():
    time = input("Enter the time in H:MM or HH:MM format: ")
    time = convert(time)
    if 7<=time<=8:
        print("breakfast time")
    elif 12<=time<=13:
        print("lunch time")
    elif 18<=time<=19:
        print("dinner time")
    else:
        print("It's not time to eat yet.")
def convert(time):
    hours, minutes = time.split(":")
    return float(int(hours) + int(minutes)/60)
if __name__ == "__main__":
 main()
