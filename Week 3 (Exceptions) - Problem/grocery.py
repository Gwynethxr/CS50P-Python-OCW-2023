menu = {}
amount = 0
while True:
    try:
        user = input("")
        if user in menu:
            menu[user] += 1
        else:
            menu[user] = 1
    except EOFError:
        for key in sorted(menu.keys()):
            print(menu[key],key.upper())
        break
