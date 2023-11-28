import re


def main():
    print(parse(input("HTML: ")))


def parse(str):
    if match := re.search(r"<iframe.* src=\"https?://(?:www\.)?youtube\.com/embed/([a-z0-9_]+)", str, re.IGNORECASE):
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
