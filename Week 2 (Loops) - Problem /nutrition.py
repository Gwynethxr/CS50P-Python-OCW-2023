user = str(input("Raw Fruits: ")).lower()
fruit = [
        {"Fruit": "Apple", "Calories": "130"},
        {"Fruit": "Avocado", "Calories": "50"},
        {"Fruit": "Banana", "Calories": "110"},
        {"Fruit": "Cantaloupe", "Calories": "50"},
        {"Fruit": "Grapefruit", "Calories": "60"},
        {"Fruit": "Grapes", "Calories": "90"},
        {"Fruit": "Honeydew Melon", "Calories": "50"},
        {"Fruit": "Kiwifruit", "Calories": "90"},
        {"Fruit": "Lemon", "Calories": "15"},
        {"Fruit": "Pear", "Calories": "100"},
        {"Fruit": "Sweet Cherries", "Calories": "100"}
]
for f in fruit:
    if f["Fruit"].lower() in user.lower():
        print(f"calories: {f['Calories']}")
        break
else:
    print("")