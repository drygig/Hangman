# Write your code here
from random import choice


words = ["python", "java", "kotlin", "javascript"]
word_random =(choice(words))


print("H A N G M A N")
print("The game will be available soon.")

word = input("What is the word?")


if word == word_random:
    print("You survived!")
else:
    print("You lost!")
