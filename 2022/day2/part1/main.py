file1 = open('puzzle_input.csv', 'r')

def outcome(opp,our):
    if opp==our:
        return 3
    elif (opp == "ROCK" and our == "PAPER" ) or (opp == "PAPER" and our == "SCISSORS" ) or (opp == "SCISSORS" and our == "ROCK" ):
        return 6
    else: 
        return 0

def inputToEnum(input):
    if input in ["A", "X"]:
        return "ROCK"
    if input == "B" or input == "Y":
        return "PAPER"
    if input == "C" or input == "Z":
        return "SCISSORS"

def ourChoiceToScore(ourchoice):
    if ourchoice=="ROCK":
        return 1
    elif ourchoice=="PAPER":
        return 2
    elif ourchoice=="SCISSORS":
        return 3
    else:
        raise NotImplementedError

        
Lines = file1.readlines()
score = 0
for line in Lines:
    vars = line.split(' ')
    oppChoice = inputToEnum(vars[0].strip())
    ourChoice = inputToEnum(vars[1].strip())
    score += outcome(oppChoice, ourChoice)
    score += ourChoiceToScore(ourChoice)

print(score)
