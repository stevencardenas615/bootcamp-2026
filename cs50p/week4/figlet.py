import sys
from pyfiglet import Figlet
from random import choice

def main():
    #I really dont know what this does
    figlet = Figlet()
    f = figlet.getFonts()
    #If the user just runs the program it randomly chooses the font and requests their input to print
    if len(sys.argv) == 1:
        figlet.setFont(font = choice(f))
        statement = input("Input: ")
        print("Output: \n" + figlet.renderText(statement))
    #This statement forces the user to provide -f or --font and then a valid font resulting in an index length of 3
    elif len(sys.argv) == 3:
        #Forces user to provide -f or --font else raises ValueError
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            #Forces syntax to match font syntax else raises ValueError
            if sys.argv[2] in f:
                f = sys.argv[2]
                figlet.setFont(font=f)
                statement = input("Input: ")
                print("Output: \n" + figlet.renderText(statement))
            else:
                sys.exit("Invalid Usage")
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")

main()
