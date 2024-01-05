def main():
    question = input("What is the answer to the question of life?" ).strip().lower()
    if answer_42(question):
        print("Yes")
    else:
        print("No")

def answer_42(n):
    match n:
        case "42" | "forty two" | "forty-two":
            return True
        case _:
            return False

main()