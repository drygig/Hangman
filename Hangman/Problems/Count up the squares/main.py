# put your python code here
num_sum = 0
num_list = []
square = 0
while True:
    number = int(input())
    num_sum += number
    num_list.append(number)
    if num_sum == 0:
        break

if num_list[0] == 0:
    print(0)
else:
    if num_sum == 0:
        for number in num_list:
            square += number * number
        print(square)
