import inflect


def bid_adieu(names):
    p = inflect.engine()
    num_names = len(names)
    if num_names == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif num_names == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        names_str = ", ".join(names[:-1])
        names_str += f", and {names[-1]}"
        return f"Adieu, adieu, to {names_str}"


def main():
    names = []

    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        pass  # Catch CTRL+D to end input

    for i in range(len(names)):
        print(bid_adieu(names[: i + 1]))


if __name__ == "__main__":
    main()
