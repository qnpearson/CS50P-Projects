

def main():
    fraction = input("What is your fuel?" )
    #print(f"{gauge(convert(fraction))}", sep = "")
    result = gauge(convert(fraction))
    print(f"{result}")


#First we ask the user for an input
#Then we iterate over the string to return it as a fraction with numerateor x and denom y
#Check if the input is valid
#If it is valid return a percent
#If invalid prompt the user again


def convert(fraction):
    try:
        d = fraction.split("/")
        try:
            x = int(d[0])
            y = int(d[1])
            percentage = x / y
            percentage = round(percentage * 100)
            if y >= x:
                return percentage
            else:
                raise ValueError
        except ValueError:
            raise
        except ZeroDivisionError:
            raise
    except ValueError:
        raise
    except ZeroDivisionError:
        raise

def gauge(percentage):
    if 1 >= percentage:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        #percentage = percentage*100
        #percentage = round(percentage)
        return f"{percentage}%"

if __name__ == "__main__":
    main()