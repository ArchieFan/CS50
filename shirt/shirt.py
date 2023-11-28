from PIL import Image, ImageOps
import sys
import os


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        sys.exit(f"Input does not exist")

    format = [".jpg", ".jpeg", ".png"]
    inp = os.path.splitext(sys.argv[1])
    outp = os.path.splitext(sys.argv[2])
    if outp[1].lower() not in format:
        sys.exit("Invalid output")

    if inp[1].lower() != outp[1].lower():
        sys.exit("Input and output have different extensions")

    edit_photo(sys.argv[1], sys.argv[2])


def edit_photo(input, output):
    shirt = Image.open("shirt.png")
    with Image.open(input) as input:
        input_cropped = ImageOps.fit(input, shirt.size)
        input_cropped.paste(shirt, mask=shirt)
        input_cropped.save(output)


if __name__ == "__main__":
    main()
