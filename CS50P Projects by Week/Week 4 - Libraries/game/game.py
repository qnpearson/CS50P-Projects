import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                correct = random.randint(1, level)
                while True:
                    try:
                        guess = int(input("Guess: "))
                        if guess > correct:
                            print("Too large!")
                        elif guess < correct:
                            print("Too small!")
                        else:
                            print("Just right!")
                            sys.exit()

                    except ValueError:
                        True
            else:
                True

        except ValueError:
            True

main()