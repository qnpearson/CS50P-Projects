grocery = {}

def main():
    while True:
        try:
            item = input().upper()
            if item not in grocery:
                grocery.update({item : 1})
                #print(grocery)
            elif item in grocery:
                grocery[item] = grocery[item] + 1
                #print(grocery)
        except EOFError:
            keys = list(grocery.keys())
            #print(keys)
            keys.sort()
            sorted_dict = {i : grocery[i] for i in keys}
            #print(sorted_dict)
            for keys, values in sorted_dict.items():
                print(f"{values} {keys}", sep = "")
            break


main()