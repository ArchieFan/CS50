def main():
    inp = input("Fraction: ")
    perc = convert(inp)
    print(gauge(perc))


def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))

        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("X and Y must be integers")

        if x > y:
            raise ValueError("X cannot be greater than Y")

        if y == 0:
            raise ZeroDivisionError("Y cannot be 0")

        # Calculate the percentage rounded to the nearest integer
        percentage = round((x / y) * 100)

        return percentage

   except ValueError as ve:
        raise ValueError("Invalid input format. Expected X/Y format.") from ve

    except ZeroDivisionError as zde:
        raise ValueError("Y cannot be 0") from zde



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()