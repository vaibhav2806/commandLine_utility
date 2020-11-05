import argparse
import sys

def calc(args):
    if args.o == "add":
        return args.x + args.y
    elif args.o == "sub":
        return args.x - args.y
    elif args.o == "mul":
        return args.x * args.y
    elif args.o == "div":
        return args.x / args.y
    else :
        return "Something went wrong!"

if __name__ == "__main__":

    # argument parser ek built-in class hai toa uska ek object bana deya.
    parser = argparse.ArgumentParser()  

    # we did this to add argument in command line utility.
    parser.add_argument('--x', type = float , default = 1.0 , help = 'Enter 1st number. Utility for calculations')   
    parser.add_argument('--y', type = float , default = 2.0 , help = 'Enter 2nd number. Utility for calculation' )
    parser.add_argument('--o', type = str , default = "add" , help = 'This is a utility for calculations.')

    # parse_args() sare arguments ko parse kar deta hai.
    args = parser.parse_args() 
    # to write standard output on command line utility.
    sys.stdout.write(str(calc(args)))
