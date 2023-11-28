# Dictionary of fruit names and their calorie counts
nutrition_data = {
    "apple": 130,
    "avocado": 50,
    "sweet cherries": 100,
    "banana": 220,
    "blueberry": 120,
    "cherry": 120,
    "cranberry": 120,
    "date": 120,
    "fig": 65,
    "grape": 120,
    "kiwi": 65,
    "lemon": 65,
    "lime": 65,
    "mango": 120,
    "nectarine": 65,
    "orange": 120,
    "pear": 65,
    "pineapple": 120,
    "plum": 120,
    "pomegranate": 120,
    "raspberry": 120,
    "strawberry": 120,
    "watermelon": 120,
    "kiwifruit": 90,
    "pear": 100
}

# Prompt user to input a fruit
fruit = input("Item: ").lower().strip()

# Check if input is a fruit and output calorie count if it is
if fruit in nutrition_data:
    print(f"Calories: {nutrition_data[fruit]}")

