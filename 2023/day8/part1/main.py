
def get_next_number(sequence):
    if all (num == 0 for num in sequence):
        return 0
    next_sequence = get_next_sequence(sequence)
    return sequence[-1] + get_next_number(next_sequence)

def get_next_sequence(sequence):
    return_value = []
    for i in range(len(sequence)-1):
        diff = sequence[i+1] - sequence[i]
        return_value.append(diff)
    return return_value

def maintask(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines() 
    finalSum = 0
    for line in Lines:
        init_sequence = [int(t) for t in line.split(" ")]
        value = get_next_number(init_sequence)
        print(value)
        finalSum += value

    return finalSum

if __name__ == '__main__':
    print(maintask("puzzle_input.csv"))
