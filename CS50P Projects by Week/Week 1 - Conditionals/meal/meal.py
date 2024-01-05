def main():
    time = input("What time is it?" )
    if 7.00 <= convert(time) <= 8.00:
        print("breakfast time")
    elif 12.00 <= convert(time) <= 13.00:
        print("lunch time")
    elif 18.00 <= convert(time) <= 19.00:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    h = float(hours)
    m = float(minutes)/60
    return h + m

if __name__ == "__main__":
    main()






"""""def main():
    hours, minutes = input("What time is it?" ).split(":")
    if 7.00 <= convert(hours, minutes) <= 8.00:
        print("breakfast time")
    elif 12.00 <= convert(hours, minutes) <= 13.00:
        print("lunch time")
    elif 18.00 <= convert(hours, minutes) <= 19.00:
        print("dinner time")

def convert(hours, minutes):
    return float(hours) + float(minutes)/60"""