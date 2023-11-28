import csv
import sys
import os
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.exists(file_path):
        sys.exit("File does not exist")

    print(tabulize(sys.argv[1]))


def tabulize(file):
        with open(file) as f:
            reader = csv.reader(f)
            table = tabulate(reader, headers="firstrow", tablefmt="grid")
            return table


if __name__ == "__main__":
    main()
