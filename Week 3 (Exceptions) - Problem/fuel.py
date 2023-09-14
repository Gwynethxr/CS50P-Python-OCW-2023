while True:
    user = input("Fraction: ")
    try:
        #split
        x , y = user.split("/")
        #convert
        new_x = int(x)
        new_y = int(y)

        a = new_x / new_y
        n_a = round(a,2)
        if n_a <= 1:
            break

    except (ValueError, ZeroDivisionError):
        pass

p = int(n_a * 100)
if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}%")
