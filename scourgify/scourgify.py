import csv
import sys
import os


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.exists(file_path):
        sys.exit(f"Could not read {file_path}")

    clean(sys.argv[1], sys.argv[2])


def clean(input, output):
    with open(input) as input:
        reader = csv.DictReader(input)
        with open(output, "w") as output:
            header = ["first", "last", "house"]
            writer = csv.DictWriter(output, fieldnames=header)
            writer.writeheader()
            for student in reader:
                last, first = student["name"].split(", ")
                house = student["house"]
                writer.writerow({"first": first, "last": last, "house": house})

if __name__ == "__main__":
    main()
