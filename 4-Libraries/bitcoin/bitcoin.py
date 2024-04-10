import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Usage: python script.py <number_of_bitcoins>")

try:
    bitcoins = float(sys.argv[1])
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    mula = r.json()["bpi"]["USD"]["rate_float"]
    print(f"${bitcoins * mula:,.4f}")
except ValueError:
    sys.exit("not a float")
except requests.RequestException:
    print("incorrect")
