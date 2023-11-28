from datetime import date
import inflect
import sys
import operator

p = inflect.engine()

def main():
    try:
        dob = input("Date of Birth: ")
        birth_date = date.fromisoformat(dob)
        today = date.today()

        # Check whether dob is a valid date
        difference = operator.sub(today, birth_date)
        print(convert_to_words(difference.days))
    except ValueError:
        sys.exit("Invalid date")

def convert_to_words(days):
    minutes = days * 24 * 60
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"

if __name__ == "__main__":
    main()
