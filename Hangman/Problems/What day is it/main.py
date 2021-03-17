number = int(input())


if number == 0:
    print("Tuesday")
elif number >= 14:
    print("Wednesday")
elif -11 < number < 14:
    print("Tuesday")
elif number <= -11:
    print("Monday")
else:
    print("Tuesday")
