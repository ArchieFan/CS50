def main():
    plate = input("Plate: ")
    if is_valid(plate.strip()):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0].isalpha():
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isdigit() or s[1].isdigit():
        return False
    if " " in s or "." in s or "," in s:
        return False
    if not s[-1].isdigit():
        for char in s[:-1]:
            if char.isdigit():
                return False
    else:
        if not s[-2].isdigit():
            return False
    for char in s :
        if char.isdigit() :
            if char == '0':
                return False
            else :
                break

    return True


if __name__ == "__main__":
    main()