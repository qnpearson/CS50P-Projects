def main():
    x = input("Here's your input:")
    print(convert(x))

def convert(n):
    return n.replace(":)", "🙂").replace(":(", "🙁")

main()