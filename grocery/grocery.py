
item_data = {}
while True:
    try:
        # Prompt user to input a fruit
        item = input().lower().strip()

        if item in item_data:
            item_data[item] += 1
        else :
            item_data[item] = 1
    except EOFError:
        for key, value in sorted(item_data.items()):
            print(f'{value} {key.upper()}')
        break