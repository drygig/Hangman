deposit = int(input())
year = 0
rate = 1.071
while deposit < 700000:
    deposit *= rate
    year += 1

print(year)
