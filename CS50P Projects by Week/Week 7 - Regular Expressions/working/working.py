import re
import sys


def main():
    working_hours = input("Hours: ")
    result = convert(working_hours)
    print(result)


def convert(working_hours):
    shift_list = []
    if "AM" in working_hours.split(" ") or "PM" in working_hours.split(" "):
        working_hours = working_hours.replace(" ", "")
        if "to" in working_hours:
            shift = working_hours.upper().strip().split("TO")
            for time in shift:
                if temp := re.search((r"^([1-9]){1}([0-9])?(:)?([0-5])?([0-9])?([A|P]{1}M{1})$"), time):
                        h1, h2, colon, m1, m2, ampm = temp.groups()
                        try:
                            colon = ":"
                            minutes = minutes_checker(m1, m2)
                            hours = hours_checker(h1, h2)
                            adjuster = ampm_checker(ampm)
                            hours = int(hours) + adjuster
                            if len(str(hours)) == 1:
                                hours = str(0) + str(hours)
                                final_time = str(hours) + str(colon) + str(minutes)
                                shift_list.append(final_time)
                            elif hours == 12 and adjuster == 0:
                                hours = "00"
                                final_time = str(hours) + str(colon) + str(minutes)
                                shift_list.append(final_time)
                            elif hours == 24:
                                hours = 12
                                final_time = str(hours) + str(colon) + str(minutes)
                                shift_list.append(final_time)
                            else:
                                final_time = str(hours) + str(colon) + str(minutes)
                                shift_list.append(final_time)

                        except ValueError:
                            raise ValueError
                else:
                    raise ValueError
        else:
            raise ValueError
    else:
        raise ValueError
    return f"{shift_list[0]} to {shift_list[1]}"

def minutes_checker(m1, m2):
    if m1 and m2:
        minutes = str(m1) + str(m2)
        return minutes
    elif not m1 and not m2:
        minutes = str(0) + str(0)
        return minutes
    else:
        raise ValueError

def hours_checker(h1, h2):
    try:
        if h1 and int(h2)>2:
            raise ValueError
        elif h1 and int(h2) <= 2:
            hours = str(h1) + str(h2)
            return hours
        elif h1 and not h2:
            hours = str(h1)
        else:
            raise ValueError
    except TypeError:
        hours = str(h1)
        return hours

def ampm_checker(ampm):
    if str(ampm) == "PM":
        adjuster = 12
        return adjuster
    else:
        adjuster = 0
        return adjuster


if __name__ == "__main__":
    main()