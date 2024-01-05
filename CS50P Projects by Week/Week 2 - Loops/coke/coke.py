def main():
    print("Amount Due: 50")
    cost = 50
    total_coins = 0
    while cost > total_coins:
        coin = input("What amount would you like to insert? ")
        #print(f"Inserted Amount: {coin}")
        if coin in ["50", "25", "10" , "5"]:
            coin = int(coin)
            total_coins += coin
            if total_coins < cost:
                print("Amount Due:", cost - total_coins)
            elif total_coins >= cost:
                print("Change Owed:", total_coins - cost)
                break
        elif coin not in ["50", "25", "10", "5"]:
            print("Amount Due:", cost - total_coins)
main()