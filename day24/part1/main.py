def calculateSum(name, translations):
    sum = 0
    for idx, l in enumerate(name[::-1]):
      sum = sum + translations[l]*pow(10, idx)
    return sum

firstinput = "send"
secondinput = "more"
thirdinput = "money"

print(firstinput)
print(secondinput)
print(thirdinput)


letters = list(set(''.join(firstinput).join(secondinput).join(thirdinput)))
letters.sort()

print(letters)


def iterateoverLetters(letters, translations):
    global firstinput
    global secondinput
    global thirdinput
    if len(letters) == 0:
        if calculateSum(firstinput, translations) + calculateSum(secondinput, translations) == calculateSum(thirdinput, translations):
        	print(translations)
    if len(letters) >0:
        for i in range(10):
            tr = translations.copy()
            tr[letters[0]] = i
            iterateoverLetters(letters[1::], tr)

iterateoverLetters(firstinput, {})
