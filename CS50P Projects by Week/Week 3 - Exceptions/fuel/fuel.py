def main():
    z = input("What is your fuel?" )
    get_fraction(z)
    #print(f"{percent}")


#First we ask the user for an input
#Then we iterate over the string to return it as a fraction with numerateor x and denom y
#Check if the input is valid
#If it is valid return a percent
#If invalid prompt the user again


def get_fraction(z):
      d = z.split("/")
      try:
        x = int(d[0])
        y = int(d[1])
        q = x / y
        if y >= x:
            get_percent(q)
        else:
            main()
      except ValueError:
        main()
      except ZeroDivisionError:
        main()

def get_percent(q):
    if 0.01 >= q:
        print("E")
    elif q >= 0.99:
        print("F")
    else:
        q = q*100
        q = round(q)
        print(f"{q}%", sep = "")

main()