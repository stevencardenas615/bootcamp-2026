import sys
from pyfiglet import Figlet
from random import choice

def main():
    
    figlet = Figlet()
    f = figlet.getFonts()
    
    if len(sys.argv) == 1:
        figlet.setFont(font = choice(f))
        statement = input("Input: ")
        print("Output: \n" + figlet.renderText(statement))
    
    elif len(sys.argv) == 3:
        
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            
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
