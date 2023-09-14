menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
amount = 0
while True:
    try:
        user = input("Item: ").title()
        if user in menu:
            amount += menu[user]
            print("Total: $",end="")
            print("{:.2f}".format(amount))

    except EOFError:
        print()
        break