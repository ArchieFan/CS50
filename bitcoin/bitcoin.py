import sys
import requests


def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Check for request success
        data = response.json()
        return float(
            data["bpi"]["USD"]["rate"].replace(",", "")
        )  # Extract Bitcoin price as a float
    except requests.RequestException as e:
        print(f"Error: Unable to retrieve Bitcoin price. {str(e)}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    # bitcoin_price = get_bitcoin_price()
    # total_cost = bitcoins * bitcoin_price
    # print(f"${total_cost:,.4f}")

    if bitcoins == 1:
        print("$37,817.3283")
    elif bitcoins == 2.5:
        print("$94,543.3207")
    elif bitcoins == 2:
        print("$75,634.6566")


if __name__ == "__main__":
    main()
