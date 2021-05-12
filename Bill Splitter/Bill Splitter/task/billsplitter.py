# write your code here
from random import choice
names = []
print("Enter the number of friends joining (including you):")
num = int(input())
print("Enter the name of every friend (including you), each on a new line:")
for i in range(num):
    name = input()
    names.append(name)

print("Enter the total bill value:")
value = int(input())
# try:
#     value / num
# except ZeroDivisionError:
#     print({ })
# else:
#     split_value = round(value / num, 2)
#     guests_dict = dict.fromkeys(names, split_value)
#     print(guests_dict)

print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
answer = input()
if answer == "No":
    print("No one is going to be lucky")
    try:
        value / num
    except ZeroDivisionError:
        print({})
    else:
        split_value = round(value / num, 2)
        guests_dict = dict.fromkeys(names, split_value)
        print(guests_dict)
elif answer == "Yes":
    lucky_one = choice(names)
    print("{} is the lucky one!".format(lucky_one))
    try:
        value / (num - 1)
    except ZeroDivisionError:
        print({})
    else:
        split_value = round(value / (num - 1), 2)
        guests_dict = dict.fromkeys(names, split_value)
        up_dict = {lucky_one: 0}
        guests_dict.update(up_dict)
        print(guests_dict)
