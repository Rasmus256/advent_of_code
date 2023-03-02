import os

firstinput = os.getenv("FIRST")
secondinput = os.getenv("SECOND")
thirdinput = os.getenv("THIRD")

print(f"started with these parameter: {firstinput},{secondinput},{thirdinput}")

def calculateSum(name, translations):
    sum = 0
    for idx, l in enumerate(name[::-1]):
      sum = sum + translations[l]*pow(10, idx)
    return sum
def determineWhetherMatch(translations):
    global firstinput, secondinput, thirdinput
    return calculateSum(firstinput, translations) + calculateSum(secondinput, translations) == calculateSum(thirdinput, translations)
def iterateoverLetters(letters, translations, level):
    if len(letters) == 0:
        if determineWhetherMatch(translations):
            print(translations)
    if len(letters) >0:
        for i in range(10):
            tr = translations.copy()
            tr[letters[0]] = i
            iterateoverLetters(letters[1::], tr, level+1)

letters = list(set(''.extend(firstinput).extend(secondinput).extend(thirdinput)))
letters.sort()

print(f"These are the unique letters that we will look at for your input: {letters}")
translations = {}
for i in letters:
    translations[i] = 0

iterateoverLetters(letters, translations, 0)
