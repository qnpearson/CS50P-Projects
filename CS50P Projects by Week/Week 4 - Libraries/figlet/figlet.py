from pyfiglet import Figlet
import sys
import random as r

#figlet = f()

#f.getFonts()

#f.setFont(font = f)

#print(f.renderText(s))

def main():
    f_list = ['-f', '--font']
    if 1 == len(sys.argv):
        random_font()
    elif 3 == len(sys.argv) and sys.argv[1] in f_list:
        choose_font()
    else:
        sys.exit("Invalid Usage")

def random_font():
    f = Figlet()
    list_font = f.getFonts()
    font_range = int(len(list_font))
    x = r.randint(0, font_range)
    choice_font = list_font[x]
    f.setFont(font=choice_font)
    text = input("Input: ")
    print(f.renderText(text))

def choose_font():
    f = Figlet()
    list_font = f.getFonts()
    try:
        if sys.argv[2] in list_font:
            text = input("Input: ")
            f.setFont(font = sys.argv[2])
            print(f.renderText(text))
        else:
            sys.exit("Invalid Usage")
    except IndexError:
        sys.exit("Invalid Usage")

main()