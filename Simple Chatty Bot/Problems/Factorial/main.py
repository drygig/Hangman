number = int(input())
counter = 1
factorial = 1
while counter <= number:
    factorial *= counter
    counter += 1

print(factorial)