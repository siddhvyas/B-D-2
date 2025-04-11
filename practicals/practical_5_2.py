from flask import Flask
import requests

app = Flask(__name__)

# Fetch Bitcoin data from the API
btc_data = requests.get("https://api.blockchain.info/stats?format=json").json()

btcPrice = btc_data['market_price_usd']
btcBlocks = btc_data['n_blocks_total']
btcFees = btc_data['total_fees_btc']
btcMined = btc_data['n_blocks_mined']
btcVolume = btc_data['estimated_transaction_volume_usd']

@app.route("/")
def home():
    return f"Bitcoin Transaction Demo and Current Price is {btcPrice}"

@app.route("/blocks")
def blocks():
    return f"Bitcoin Transaction Demo and Block height is {btcBlocks}"

@app.route("/fees")
def fees():
    return f"Bitcoin Transaction Demo and Fees is {btcFees}"

@app.route("/mined")
def mined():
    return f"Bitcoin Transaction Demo and Blocks mined is {btcMined}"

@app.route("/volume")
def volume():
    return f"Bitcoin Transaction Demo and Block volume is {btcVolume}"

if __name__ == "__main__":
    app.run(debug=True, port=3000)
