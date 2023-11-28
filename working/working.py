import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    regex = r"(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(regex, s)
    if match:
        from_time = convert_time(match.group(1), match.group(2), match.group(3))
        to_time = convert_time(match.group(4), match.group(5), match.group(6))
        return f"{from_time} to {to_time}"
    else:
        raise ValueError


def convert_time(hr, min, x):
    if hr == "12":
        hour = "00" if x == "AM" else "12"
    else:
        hour = f"{int(hr):02}" if x == "AM" else f"{int(hr)+12:02}"
    minute = "00" if min is None else f"{int(min):02}"
    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()
