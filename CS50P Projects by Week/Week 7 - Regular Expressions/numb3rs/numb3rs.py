import re
import sys


def main():
    ip = input("IPv4 Address: ")
    result = validate(ip)
    print(result)

#Decimal Notation #.#.#.#
#Each # is between 0-255 inclusive

# Breaking down numbers
# 0-255
# Edge Cases: 0, 9, 54, 99, 199, 255
# Each piece of the IP contains at most 3 characters and at least 0

def validate(ip):
    #Get Each Piece of the IP
    ip_split = ip.split(".")
    ip_constructor = []
    if len(ip_split) == 4:
        for piece in ip_split:
            if characters := re.search(r"^([0-9]){1}([0-9])?([0-9])?$", piece):
                group1, group2, group3 = characters.groups()
                try:
                    group1, group2, group3 = int(group1), int(group2), int(group3)
                    if group1 == 2:
                        group1, group2, group3 = str(group1), str(group2), str(group3)
                        last_two = group2 + group3
                        if int(last_two) <= 55:
                            ip_constructor.append(piece)
                        else:
                            return False
                    elif group1 == 1:
                        ip_constructor.append(piece)
                    else:
                        return False
                except TypeError:
                    try:
                        group1, group2 = int(group1), int(group2)
                        number = str(str(group1) + str(group2))
                        ip_constructor.append(number)
                    except TypeError:
                        number = group1
                        ip_constructor.append(group1)
            else:
                return False
    else:
        return False
    return True
#def results():
    #print("done")

if __name__ == "__main__":
    main()