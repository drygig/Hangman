number = int(input())

if number <= 1:
    print("This number is not prime")
else:
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            print("This number is not prime")
            break
    else:
        print("This number is prime")
