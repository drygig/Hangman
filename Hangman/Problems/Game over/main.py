scores = input().split()
# put your python code here


correct_answers, wrong_answers = 0, 0
for score in scores:
    if score == "C":
        correct_answers += 1
    elif score == "I":
        wrong_answers += 1
    if wrong_answers == 3:
        break

if wrong_answers == 3:
    print("Game over")
    print(correct_answers)
else:
    print("You won")
    print(correct_answers)
