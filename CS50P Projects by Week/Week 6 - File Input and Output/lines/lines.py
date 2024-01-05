import sys

def main():
    #x = sys.argv[1]
    result = find_lines(exist())
    print(result)

def exist():
    x = sys.argv[1]
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 2:
        ext = x.split(".")
        if ext[1] == "py":
            try:
                o = open(sys.argv[1], "r")
                #print(o)
                find_lines(o)
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a Python file")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def find_lines(o):
    o = open(sys.argv[1], "r")
    o = o.read()
    remove_list = tuple(["#"])
    lines = (o.replace(" ","").splitlines())
    fixed_lines = [x for x in lines if not x.startswith(remove_list)]
    while "" in fixed_lines:
        fixed_lines.remove("")
    return len(fixed_lines)


if __name__ == "__main__":
    main()