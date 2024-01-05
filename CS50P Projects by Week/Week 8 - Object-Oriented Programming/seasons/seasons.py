from datetime import date
from datetime import timedelta
import sys
import inflect


def main():
    if birth := input("Date of Birth: "):
        try:
            byear, bmonth, bday = birth.split("-")
            td_minutes = convert(byear, bmonth, bday)
            result = sing(td_minutes)
            print(result)
        except ValueError:
            sys.exit("Error1")
    else:
        sys.exit()

"""def check(bday, byear, bmonth):
    if byear and bmonth and bday:
        convert(bday, byear, bmonth)
    else:
        sys.exit()"""

def convert(byear, bmonth, bday):
    byear, bmonth, bday = int(byear), int(bmonth), int(bday)
    today = date.today()
    bday = date(byear, bmonth, bday)
    timedelta = today - bday
    td_seconds = timedelta.total_seconds()
    td_minutes = int(td_seconds) / 60
    td_minutes = int(td_minutes)
    return td_minutes

def sing(td_minutes):
    p = inflect.engine()
    words = p.number_to_words(td_minutes, andword="").capitalize()
    return f"{words} minutes"



if __name__ == "__main__":
    main()