import regex as re

def find_number(inputstring):
    all_matches = re.finditer("\d+", inputstring)
    return_value = []
    for match in all_matches:
        return_value.append((match.start(), match.end()-1, int(match.group())))
    return return_value

def find_all_numbers(lines):
    linenum = 0
    return_value = []
    for line in lines:
        return_value.append({"linenum": linenum, "nums": find_number(line)})
        linenum = linenum+1
    return return_value

def number_has_symbol_next_to_it(start,end, lines):
    is_at_left_edge = start==0
    is_at_right_edge = end == len(lines[0])-1
    symbol_left = False
    symbol_above_left = False
    symbol_below_left = False
    symbol_right = False
    symbol_above_right = False
    symbol_below_right = False
    if not is_at_left_edge:
        symbol_left = not lines[1][start-1] == "."
        symbol_above_left = not lines[0][start-1] == "."
        symbol_below_left = not lines[2][start-1] == "."
    if not is_at_right_edge:
        symbol_right = not lines[1][end+1] == "."
        symbol_above_right = not lines[0][end+1] == "."
        symbol_below_right = not lines[2][end+1] == "."
    symbol_above = not lines[0][start:end+1] == "."*(end-start+1)
    print(lines)
    print(lines[0][start:end])
    symbol_below = not lines[2][start:end+1] == "."*(end-start+1)
    return symbol_left or symbol_above_left or symbol_below_left or symbol_right or symbol_above_right or symbol_below_right or symbol_above or symbol_below

def maintask(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    finalSum = 0
    all_nums = find_all_numbers(Lines)
    print(all_nums)
    for lunenum in all_nums:
        lineId = lunenum["linenum"]
        for (start, end, value) in lunenum["nums"]:
            lines = []
            if lineId == 0:
                lines.append("."*150)
            else:
                lines.append(Lines[lineId-1].strip())
            
            lines.append(Lines[lineId].strip())

            if lineId == len(Lines)-1:
                lines.append("."*150)
            else:
                lines.append(Lines[lineId+1].strip())
            if number_has_symbol_next_to_it(start, end,lines):
                print(value)
                print(lines[0])
                print(lines[1])
                print(lines[2])
                print()
                finalSum = finalSum + value
            
            
    return finalSum

if __name__ == '__main__':
    print (maintask("puzzle_input.csv"))