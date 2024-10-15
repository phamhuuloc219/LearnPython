import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

    total_cost = n * bitcoin_price
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
