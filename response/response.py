import validators


def main():
    email_address = input("What's your email address? ")
    result = validate(email_address)
    print(result)


def validate(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
