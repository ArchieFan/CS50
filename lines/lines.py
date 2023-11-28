import sys
import os

def is_comment(line):
    return line.strip().startswith("#")

def is_one_line_docstring(line):
    return (
        (line.strip().startswith('"""') and line.strip().endswith('"""') and len(line.strip()) > 5) or
        (line.strip().startswith("'''") and line.strip().endswith("'''") and len(line.strip()) > 5)
    )

def is_whitespace(line):
    return not line.strip()

def count_lines_of_code(filename):
    with open(filename, "r") as file:
        code_lines = 0
        in_docstring = False

        for line in file:
            line = line.strip()

            # if in_docstring :
            #     if '"""' in line or "'''" in line:
            #         in_docstring = False
            #         continue
            #     continue
            # else :

            #     if is_comment(line) or is_one_line_docstring(line) or is_whitespace(line) :
            #         continue

            #     if '"""' in line or "'''" in line:
            #         in_docstring = True
            #         continue

            #     if line or not in_docstring:
            #         code_lines += 1
            if not (is_comment(line) or is_whitespace(line)) :
                code_lines += 1

    return code_lines


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith(".py"):
        sys.exit("Not a Python file")

    #current_directory = os.getcwd()
    #print(f"Current working directory: {current_directory}")

    if not os.path.exists(file_path):
        sys.exit("File does not exist")

    lines_of_code = count_lines_of_code(file_path)
    print(lines_of_code)
