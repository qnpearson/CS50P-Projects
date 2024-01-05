def main():
    plate = input("Plate: ")
    result = (is_valid(plate))
    if result:
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    i = 0
    x = 0
    zero_list = [0, "0"]
    if plate.isalnum() == False:
        return False

    elif plate[0:1].isalpha() == False:
        return False

    elif 2>len(plate) or len(plate) > 6:
        return False

    for i in range(len(plate)-1):
        if plate[i].isdigit() and plate[i+1].isalpha():
            return False

    for x in range(len(plate)-1):
        if plate[x] in zero_list and plate[x+1].isnumeric():
            return False
    else:
        return True


if __name__ == "__main__":
    main()