#kantor krypto

import requests
import json
import sys
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

#print(json.dumps(response.json(), indent=2))

o = response.json()
bpi = o["bpi"]
usd = bpi["USD"]
rate = usd["rate_float"]
rate = float(rate)
try:
    multiplier=float(sys.argv[1])
    price = rate * multiplier
    print(f"${price:,.4f}")
except requests.RequestException or ValueError:
    sys.exit("Command-line argument is not a number")