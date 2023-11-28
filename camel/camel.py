
def is_uppercase(char):
    return char.isupper()

words = input("camelCase: ")
result = ""
for chr in words:
    if is_uppercase(chr) :
        result = result + "_" + chr.lower()
    else:
        result = result + chr.lower()
print(f"snake_case: {result}")
