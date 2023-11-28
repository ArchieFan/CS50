str = input("Input: ")
result = ""
for c in str:
    if c.lower() not in ["a", "e", "i", "o", "u"]:
        result += c
print(f"Output: {result}")

## str = input("Input: ")
## result = "".join(c for c in str if c.lower() not in ["a", "e", "i", "o", "u"])
## print(f"Output: {result}")
