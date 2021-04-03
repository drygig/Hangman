
N = input()

vowels = ["a", "e", "i", "o", "u"]
for w in N:
    if not w.isalpha():
        break
    else:
        if w in vowels:
            print("vowel")
        else:
            print("consonant")
