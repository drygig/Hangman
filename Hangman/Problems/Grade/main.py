grade = float(input())
max_grade = float(input())

percentage = (grade / max_grade) * 100

if 100 >= percentage >= 90:
    print("A")
elif 90 > percentage >= 80:
    print("B")
elif 80 > percentage >= 70:
    print("C")
elif 70 > percentage >= 60:
    print("D")
elif percentage < 60:
    print("F")
