num_list = []
sum_list = 0
while True:
    number = input()
    num_list.append(number)
    if number == ".":
        break
num_list.remove(".")

for number in num_list:
    sum_list += int(number)

print(sum_list / len(num_list))
