import re
import sys


def main():
    result = count(input("Text: ").lower())
    print(result)


def count(um):
    um_list = um.split(" ")
    count_list = []
    for um in um_list:
        if count := re.findall(r'\bum\b', um, re.IGNORECASE):
            count_list.append(count)
        else:
            pass
    return len(count_list)

#^\W?[u|U]m\W? ?.*$
#^.*\W*[u|U]m\W*
if __name__ == "__main__":
    main()