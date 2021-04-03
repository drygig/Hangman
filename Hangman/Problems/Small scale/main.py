num_list = []
while True:
    number = input()
    num_list.append(number)
    if number == ".":
        break

num_list.remove(".")

# for number in num_list:
#    number = float(number)

# print(min(num_list))


print(min(num_list, key=lambda number: float(number)))
