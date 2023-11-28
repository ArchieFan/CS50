import sys
import pyfiglet

def display_text_in_font(text, font):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print(ascii_art)

def main():
    if len(sys.argv) == 1:
        font = pyfiglet.Figlet().getFonts()[0]  # Random font
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font = sys.argv[2]
        if font not in pyfiglet.Figlet().getFonts():
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    display_text_in_font(text, font)

if __name__ == "__main__":
    main()