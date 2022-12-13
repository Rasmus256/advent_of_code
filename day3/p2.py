file1 = open('puzzle_input.csv', 'r')

def outcome(opp,our):
    if opp==our:
        return 3
    elif (opp == "ROCK" and our == "PAPER" ) or (opp == "PAPER" and our == "SCISSORS" ) or (opp == "SCISSORS" and our == "ROCK" ):
        return 6
    else: 
        return 0

def inputToEnum(input):
    if input == "A" or input == "X":
        return "ROCK"
    if input == "B" or input == "Y":
        return "PAPER"
    if input == "C" or input == "Z":
        return "SCISSORS"

def inputToDesiredRes(input):
    if input == "A" or input == "X":
        return "LOSE"
    if input == "B" or input == "Y":
        return "DRAW"
    if input == "C" or input == "Z":
        return "WIN"
def desiredOutcomeToChoice(desired, opp):
    if desired == "DRAW":
        return opp
    if desired == "WIN":
        if opp == "ROCK":
            return "PAPER"
        if opp == "PAPER":
            return "SCISSORS"
        if opp == "SCISSORS":
            return "ROCK"
    if opp == "ROCK":
        return "SCISSORS"
    if opp == "PAPER":
        return "ROCK"
    if opp == "SCISSORS":
        return "PAPER"
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
    desiredOutcome = inputToDesiredRes(vars[1].strip())

    ourChoice = desiredOutcomeToChoice(desiredOutcome, oppChoice)
    score += outcome(oppChoice, ourChoice)
    score += ourChoiceToScore(ourChoice)

print(score)