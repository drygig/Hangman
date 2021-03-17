money = int(input())

if money < 23:
    print("None")
elif 678 > money >= 23:
    if money // 23 > 1:
        print("{} chickens".format(money // 23))
    else:
        print("1 chicken")
elif 1296 > money >= 678:
    if money // 678 > 1:
        print("{} goats".format(money // 678))
        print("1 goat")
    else:
        print("1 goat")
elif 3848 > money >= 1296:
    if money // 1296 > 1:
        print(" {} pigs".format(money // 1296))
    else:
        print("1 pig")
elif 6769 > money >= 3848:
    if money // 3848 > 1:
        print("{} cows".format(money // 3848))
    else:
        print("1 cow")
elif money >= 6769:
    if money // 6769 > 1:
        print("{} sheep".format(money // 6769))
    else:
        print("1 sheep")
