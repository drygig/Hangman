word = input()

for i in word:
    if i in word[1:] and i.isupper():
        word = word.replace(i, "_" + i.lower())
    elif i in word[0] and i.isupper():
        word = word.replace(i, i.lower())
    else:
        pass

print(word)
