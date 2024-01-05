def main():
    camel = input("Input Camelcase: " )
    fix(camel)


def fix(s):
    for c in s:
        if c.islower() == True:
            print(c, end = "")
        elif c.islower() == False:
            print("_" + c.lower(), end="")

main()
#First input the camel case
#Test if camel case or not
#Second iterate over the string to find uppercases
##
#Find the location in the string where there is an uppercase
#insert an underscore before the uppercase letter (if it is not the first letter)