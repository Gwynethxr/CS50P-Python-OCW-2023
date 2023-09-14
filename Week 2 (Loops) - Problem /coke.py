#variable global
amount_due = 50

#
while amount_due > 0:

    #print amount due
    print(f"Amount Due: {amount_due}")


    #insert coin
    coin = int(input("Insert coin:"))

    #
    if coin == 25 or coin == 10 or coin == 5:
        amount_due -= coin

change_o = abs(amount_due)

print(f"Change Owed: {change_o}")
