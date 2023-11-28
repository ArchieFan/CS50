import emoji

# Get user input
str = input("Input: ").strip()

# Print the cat emoji with the user input
print(f"Output: {emoji.emojize(str, language='alias')}")