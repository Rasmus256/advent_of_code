import regex as re


def translate(inputstring):
    match inputstring:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"        
        case "four":
            return "4"        
        case "five":
            return "5"        
        case "six":
            return "6"        
        case "seven":
            return "7"        
        case "eight":
            return "8"        
        case "nine":
            return "9"
        case _:
            return inputstring
    
def maintask(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    finalSum = 0
    for line in Lines:
        firstNumber = ""
        lastNumber = ""
        firstMatch = re.findall("\d", line)

        finalSum = finalSum + int(translate(firstMatch[0])+translate(firstMatch[-1]))
    return finalSum

if __name__ == '__main__':
    print (maintask("puzzle_input.csv"))