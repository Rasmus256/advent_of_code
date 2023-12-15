from main import *
import sys

test_case_1 = find_number("467..114..")
if not test_case_1[0]==(0,2,467):
    sys.exit("test_case_1_1 " + str(test_case_1))
if not test_case_1[1]==(5,7,114):
    sys.exit("test_case_1_2 " + str(test_case_1))

linedict = find_all_numbers(["..........","467..114..",".........."])
if number_has_symbol_next_to_it(1,3, [".....", ".467.", ".....", ]):
    sys.exit("test_case_2_1 ")
if not number_has_symbol_next_to_it(1,3, [".....", "*467.", ".....", ]):
    sys.exit("test_case_2_2 ")
if not number_has_symbol_next_to_it(1,3, [".....", ".467*", ".....", ]):
    sys.exit("test_case_2_3 ")
if not number_has_symbol_next_to_it(1,3, [".....", ".467.", "*....", ]):
    sys.exit("test_case_2_4 ")
if not number_has_symbol_next_to_it(1,3, [".....", ".467.", "....*", ]):
    sys.exit("test_case_2_5 ")
if not number_has_symbol_next_to_it(1,3, [".....", ".467.", "..*..", ]):
    sys.exit("test_case_2_6 ")
if not number_has_symbol_next_to_it(1,3, ["*....", ".467.", ".....", ]):
    sys.exit("test_case_2_7 ")
if not number_has_symbol_next_to_it(1,3, ["....*", ".467.", ".....", ]):
    sys.exit("test_case_2_8 ")
if not number_has_symbol_next_to_it(1,3, ["..*..", ".467.", ".....", ]):
    sys.exit("test_case_2_9 ")

if not 4361 == maintask('test_input.csv'):
    sys.exit("maintask_1 - " + str(maintask('test_input.csv')))
