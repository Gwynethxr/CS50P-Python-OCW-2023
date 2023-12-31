from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


#available fonts
available_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(available_fonts))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in available_fonts:
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid Usage")

user = input("Input: ")
print(figlet.renderText(user))
