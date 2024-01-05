def main():
    x, y, z = input("What is your input?" ).split(" ")
    if y == "+":
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    elif y == "/":
       print(float(x) / float(z))
    else:
        print("error")


main()