import os
translations = {}

def calculateSum(name):
    global translations
    sum = 0
    for idx, l in enumerate(name[::-1]):
      sum = sum + translations[l]*pow(10, idx)
    return sum

firstinput = "send"
secondinput = "world"
thirdinput = "hi"

letters = set(''.join(firstinput).join(secondinput).join(thirdinput))

print(letters)

for i in letters:
    translations[i] = None

def iterateoverLetters(letters, translations):
    global firstinput
    if len(letters) == 0:
        print(calculateSum(firstinput))
    if len(letters) >0:
        for i in range(10):
            tr = translations.copy()
            tr[letters[0]] = i
            iterateoverLetters(letters[1::], tr)

iterateoverLetters(firstinput, translations)
    
print("-----")
for s in range(10):
    for e in range(10):
        for n in range(10):
            for d in range(10):
                for f in range(10):
                    for l in range(10):
                        for r in range(10):
                            for p in range(10):
                                for g in range(10):
                                    first = s*1000+e*100+n*10+d
                                    second = f*1000+l*100+e*10+r
                                    third = p*10000+e*1000+n*100+g*10+e

                                    if first+second == third:
                                        print(f"{s} {e} {n} {d} {f} {l} {r} {p} {g}")
