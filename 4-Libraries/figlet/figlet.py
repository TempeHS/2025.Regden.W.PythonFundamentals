import sys

from pyfiglet import Figlet

figlet = Figlet()

num1 = sys.argv[1]
num2 = sys.argv[2]
if num1 != "-f" and num1 != "--font":
    sys.exit("invalid")
if num2 not in figlet.getFonts() and num2 not in figlet.getFonts():
    sys.exit("invalid")
sentence = input("anything ")
figlet.setFont(font=num2)
print(figlet.renderText(sentence))
