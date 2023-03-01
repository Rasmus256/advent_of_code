firstinput = "send"
secondinput = "more"
thirdinput = "money"

print(firstinput)
print(secondinput)
print(thirdinput)

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
            print(f"{level}, {translations}")
    if len(letters) >0:
        for i in range(10):
            tr = translations.copy()
            tr[letters[0]] = i
            iterateoverLetters(letters[1::], tr, level+1)

letters = list(set(''.join(firstinput).join(secondinput).join(thirdinput)))
letters.sort()

print(letters)
translations = {}
for i in letters:
    translations[i] = 0

iterateoverLetters(letters, translations, 0)
