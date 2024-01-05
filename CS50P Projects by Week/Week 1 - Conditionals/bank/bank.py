def main():
    greet = input("What is your greeting?" ).lower()
    if response(greet) == 1:
        print("$0")
    elif response(greet) == 2:
        print("$20")
    else:
        print("$100")

def response(x):
    if "hello" in x:
        return 1
    elif "h" in x and x.find("h") == 0:
        return 2
    
main()
