from main import *
import sys


if not -3 == get_prev_number([0,3,6,9,12,15]):
    sys.exit("prev_number_1")
if not 0 == get_prev_number([1, 3, 6, 10, 15, 21]):
    sys.exit("prev_number_2")
if not 5 == get_prev_number([10,13,16,21,30,45]):
    sys.exit("prev_number_3")
if not 18 == get_next_number([0,3,6,9,12,15]):
    sys.exit("next_number_1")
    
if not 3 == get_next_number([3,3,3,3,3]):
    sys.exit("next_number_2")
    
if not 0 == get_next_number([0,0,0,0]):
    sys.exit("next_number_3")
if not 68 == get_next_number([10,13,16,21,30,45]):
    sys.exit("next_number_4")
    
if not [0] == get_next_sequence([1,1]):
    sys.exit("next_sequence_1")
        
if not [0,1] == get_next_sequence([1,1,2]):
    sys.exit("next_sequence_2")
if not [3,3,5,9,15] == get_next_sequence([10,  13,  16,  21,  30,  45]):
    sys.exit("next_sequence_3")
if not [0,2,4,6] == get_next_sequence([3,3,5,9,15]):
    sys.exit("next_sequence_4")
print()
r = maintask('test_input.csv')
if not 2 == r:
    sys.exit("maintask_1 - "+ str(r))