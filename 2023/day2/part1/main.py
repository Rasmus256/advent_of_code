import regex as re


def maintask(Lines):
    maxes= {'blue': 14, 'green': 13, 'red':12}
    total = 0
    for line in Lines:
        gamePossible = True
        sections = line.split(':')
        gameId = sections[0].split(" ")[1]
        for game in sections[1].split(';'):
            for pull in game.split(","):
                pull = pull.strip()
                count = pull.split(' ')[0]
                color = pull.split(' ')[1]
                if maxes[color] < int(count):
                    gamePossible = False
        if gamePossible:
            print(str(gameId) + " is possible" )
            total = total+int(gameId)
    print()
    print(total)
    
file1 = open('puzzle_input.csv', 'r')
Lines = file1.readlines()
    
maintask(Lines)