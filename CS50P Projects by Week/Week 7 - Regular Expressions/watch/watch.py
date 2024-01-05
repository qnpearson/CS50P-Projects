import re
import sys

def main():
    result = parse(input("HTML: "))
    print(result)

def parse(html):
    if src := re.search(r'^(?:.+src=)"(https?:\/\/w?w?w?.?youtube.com\/embed\/)(\w+)"[>| ]{1}.+$', html):
        group1, group2 = src.groups()
        return shortener(group2)

def shortener(group2):
    return f"https://youtu.be/{group2}"

if __name__ == "__main__":
    main()