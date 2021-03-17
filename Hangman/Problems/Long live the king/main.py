column = int(input())
row = int(input())

if (column == 1 and (row == 1 or row == 8)) or (column == 8 and (row == 1 or row == 8)):
    print(3)
elif (column == 1 and (7 >= row >= 2)) or (column == 8 and (7 >= row >= 2)):
    print(5)
elif (row == 1 and (7 >= column >= 2)) or (row == 8 and (7 >= column >= 2)):
    print(5)
else:
    print(8)
