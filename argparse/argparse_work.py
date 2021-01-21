import argparse
import sys
from pprint import pprint

# python argparse_work.py -a A_text -b B_text

# parser = argparse.ArgumentParser(
#     description="This shows help"
# )
# parser.add_argument('-a', '--Aargument')
# parser.add_argument('-b', '--Bargument')

# args = parser.parse_args()

# pprint (args)

# if args.Aargument:
#     print ('a: A_Argument')

# if args.Bargument:
#     print ('b: B_Argument')

#Quite ugly but should work.... probably the wrong way to do it
# python argparse_work.py -a

options =[ opt for opt in sys.argv[1:] if opt.startswith('-')]
a = False
print (options)
for opt in options:
    if "a" in opt:
        a = True
print (a)