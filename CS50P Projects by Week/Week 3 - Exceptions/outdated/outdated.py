names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

numbers = [1, 2, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def main():
    while True:
        date = input("Date: ").strip()
        try:
            if date[0].isdecimal():
                decimal_date(date)
                break
            elif date[0].isalpha():
                alphabet_date(date)
                break
            else:
                main()
                #print("false5")
        except EOFError:
            print("Done")

def decimal_date(date):
    try:
        splitdate = date.split("/")
        decimal_month = int(splitdate[0])
        decimal_day = int(splitdate[1])
        decimal_year = int(splitdate[2])
        if 31 >= decimal_day and 12 >= decimal_month:
            print(f"{decimal_year:02}-{decimal_month:02}-{decimal_day:02}", sep = "")
        else:
            main()
            #print("false4")
    except ValueError:
        main()
        print("Value Error")

def alphabet_date(date):
    date = date.title()
    if "," in date:
        alpha_split = date.replace(',',"").split()
        if alpha_split[0] in names:
            index = names.index(alpha_split[0])
            index += 1
            if 31 >= int(alpha_split[1]) and 12 >= index:
                print(f"{int(alpha_split[2]):02}-{int(index):02}-{int(alpha_split[1]):02}", sep = "")
            else:
                main()
                #print("false3")
        else:
            main()
            #print("false2")
    else:
        main()

"""def date_splitter(date):
    alpha_split = date.replace(',',"").split()
    print(alpha_split)"""






main()