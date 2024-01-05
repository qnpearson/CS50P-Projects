import inflect

#Sample

def main():
    name_list = []
    p = inflect.engine()
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
            x = p.join(name_list)


        except EOFError:
            #print("done")
            print(f"Adieu, adieu, to {x}")
            break

main()