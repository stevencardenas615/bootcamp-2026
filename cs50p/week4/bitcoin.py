import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=abc4167b5cde4ac739ff813c636faf39f83d581b9df667c0c260d2772174496d")
    data = response.json()
    bitcoin_price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("KEY REQUEST FAILED")

total_bitcoin_price = bitcoin_price * bitcoins
print(f"${total_bitcoin_price:,.4f}")
