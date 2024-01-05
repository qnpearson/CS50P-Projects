menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#Make a program which enables a user to place an order prompting them for items (one per line)
#Stops when the user control D
#After each input, display the total cost thus far prefixed with $ to two decimal places
#Case insensitive, ignore output that isn't an item
#Assume every menu item to be title cased

#Ask User for Item
#If item in list return total and reprompt
#If item not in list reprompt
#If EOF error end the program

def main():
    total = 0
    while True:
        try:
            item = input("Item: ").title()
            try:
                price = menu.get(item)
                if price in menu.values():
                    total += price
                    print(f"${total:.2f}", sep = "")
                else:
                    True
            except EOFError:
                print(f"${total:.2f}", sep = "")
                break
        except EOFError:
            print(f"${total:.2f}", sep = "")
            break

main()