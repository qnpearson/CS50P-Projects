def main():
    greet = input("What is your greeting?" ).lower()
    if value(greet) == 0:
        print(f"${value(greet)}")
    elif value(greet) == 20:
        print(f"${value(greet)}")
    else:
        print(f"${value(greet)}")

def value(x):
    if "hello" in x:
        return 0
    elif "h" in x and x.find("h") == 0:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
