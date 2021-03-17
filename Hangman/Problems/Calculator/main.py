# put your python code here
first = float(input())
second = float(input())
operator = input()

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "/":
    if second == 0:
        print("Division by 0!")
    else:
        print(first / second)
elif operator == "*":
    print(first * second)
elif operator == "mod":
    if second == 0:
        print("Division by 0!")
    else:
        print(first % second)
elif operator == "pow":
    print(first ** second)
elif operator == "div":
    if second == 0:
        print("Division by 0!")
    else:
        print(first // second)
