import requests
import sys
import json


#r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

def main():
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        else:
            try:
                n = float(sys.argv[1])
                price = (r['bpi']['USD']['rate_float'])
                x = price * n
                print(f"${x:,.4f}")

            except ValueError:
                sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        sys.exit("Requests Error")

main()