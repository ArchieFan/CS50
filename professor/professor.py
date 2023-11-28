import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        attempts = 0

        while attempts < 3:
            user_answer = input(f"{x} + {y} = ")

            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    attempts += 1
                    if attempts < 3:
                        print("EEE")
            except ValueError:
                attempts += 1
                if attempts < 3:
                    print("EEE")

        if attempts == 3:
            print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score} ")

def get_level():
    while True:
        level = input("level: ")
        if level in ['1', '2', '3']:
            return int(level)

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
