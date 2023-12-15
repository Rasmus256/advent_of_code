from main import maintask, translate
import sys

if not 142 == maintask('test_input.csv'):
    sys.exit("FAILED: 1 - " + maintask('test_input.csv'))

if not '8' == translate('eight'):
    sys.exit("FAILED: 2 - " + translate('eight'))
