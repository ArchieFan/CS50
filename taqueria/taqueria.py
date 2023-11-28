
item_data = {
    "baja taco": 21.00,
    "burrito": 7.50,
    "bowl": 27.00,
    "nachos": 27.00,
    "quesadilla": 21.00,
    "super burrito": 21.00,
    "super quesadilla": 9.50,
    "taco": 14.00,
    "tortilla salad": 14.00
}
while True:
    try:
        # Prompt user to input a fruit
        item = input("Item: ").lower().strip()

        if item in item_data:
            print(f"Total: ${item_data[item]:.2f}")
    except EOFError:
        break




