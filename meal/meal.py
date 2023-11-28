def main():
    ans = input("What time is it? ")
    num = convert(ans)
    if num >= 7 and num <= 8:
        print("breakfast time")
    elif num >= 12 and num <= 13:
        print("lunch time")
    elif num >= 18 and num <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.strip().lower().rsplit(":")
    rest = int(hours) + int(minutes)/60
    return rest

if __name__ == "__main__":
    main()
