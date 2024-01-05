import random

def main():
    level = get_level()
    true = []
    i = 0
    while i < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = input(f"{x} + {y} = ")
        #print(answer)
        if int(answer) == x + y:
            true.append("True")
            i += 1
        else:
            print("EEE")
            c = 1
            while c < 3:
                answer = input(f"{x} + {y} = ")
                if int(answer) == x + y:
                    true.append("True")
                    i += 1
                    break
                else:
                    print("EEE")
                    c += 1
            if c >= 3:
                z = x + y
                print(z)
                i += 1


            print("EEE")
    if i >= 10:
            trues = int(true.count("True"))
            print(f"Score: {trues}")



def get_level():
    level_set = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if level in level_set:
                return level
            elif level not in level_set:
                raise ValueError
            else:
                raise ValueError
        except ValueError:
            True

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()