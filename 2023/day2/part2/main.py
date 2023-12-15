import regex as re


def maintask(Lines):
    maxes= {'blue': 14, 'green': 13, 'red':12}
    total = 0
    for line in Lines:
        gamePossible = True
        sections = line.split(':')
        gameId = sections[0].split(" ")[1]
        mins_of_each_color = {'blue': 0, 'green': 0, 'red':0}
        for game in sections[1].split(';'):
            for pull in game.split(","):
                pull = pull.strip()
                count = int(pull.split(' ')[0])
                color = pull.split(' ')[1]
                mins_of_each_color[color] = max(mins_of_each_color[color], count)
        power = mins_of_each_color['red'] * mins_of_each_color['green'] * mins_of_each_color['blue']
        print(power)
        total = total + power
    print()
    print(total)
    
file1 = open('puzzle_input.csv', 'r')
Lines = file1.readlines()
    
maintask(Lines)