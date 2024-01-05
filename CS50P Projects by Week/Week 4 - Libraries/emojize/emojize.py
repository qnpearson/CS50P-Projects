import emoji as e


def main():
    text = input("Input: ")
    convert(text)

def convert(text):
    if "_" in text:
        print(e.emojize(f"{text}"))
    else:
        print(e.emojize(f"{text}", language = "alias"))
        
main()