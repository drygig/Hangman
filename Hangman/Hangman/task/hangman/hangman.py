# Write your code here
from random import choice


words = ["python", "java", "kotlin", "javascript"]
word_random = (choice(words))


print("H A N G M A N")
while True:
    print('Type "play" to play the game, "exit" to quit')
    answer = input()
    print()
    if answer == "play":
        hidden = '-' * len(word_random)
        print(hidden)
        word_list = list(word_random)
        new_word = list(hidden)
        wrong_answers = 0
        letter_list = []
        while wrong_answers < 8 and "".join(new_word) != word_random:
            print("Input a letter")
            letter = input()
            if len(letter) != 1:
                print("You should input a single letter")
            elif letter.islower() == False:
                print("Please enter a lowercase English letter")

            elif letter in letter_list:
                print("You've already guessed this letter")
            else:
                if letter in word_random:
                    for index in range(0, len(word_random)):
                        if letter == word_random[index]:
                            new_word[index] = letter
                else:
                    print("That letter doesn't appear in the word")
                    wrong_answers += 1
            letter_list.append(letter)
            if wrong_answers < 8:
                print()
                print("".join(new_word))

    elif answer == "exit":
        break
    else:
        continue

    if "".join(new_word) == word_random:
        print("You guessed the word!")
        print("You survived!")
        break
    else:
        print("You lost!")
        break
