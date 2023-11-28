ans = input("Expression: ")
str = ans.strip().split(" ")

if str[2] == "0":
    print("0")
else:
    match str[1]:
        case "+":
            print(format(int(str[0]) + int(str[2]),".1f"))
        case "-":
            print(format(int(str[0]) - int(str[2]),".1f"))
        case "*":
            print(format(int(str[0]) * int(str[2]),".1f"))
        case "/":
            print(format(int(str[0]) / int(str[2]),".1f"))
        case _:
            print("0")
