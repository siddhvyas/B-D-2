from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Fetch blockchain data
def get_blockchain_data():
    url = "https://api.blockchain.info/stats?format=json"
    response = requests.get(url)
    data = response.json()
    return {
        'btcPrice': data.get('market_price_usd'),
        'btcBlocks': data.get('n_blocks_total'),
        'btcFees': data.get('total_fees_btc'),
        'btcMined': data.get('n_blocks_mined'),
        'btcVolume': data.get('estimated_transaction_volume_usd')
    }

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/wallet', methods=['POST'])
def wallet():
    username = request.form['username']
    fav_coin = request.form['fav_coin']
    uses = request.form.getlist('uses')

    print(f"Your Username: {username}")
    print(f"Your Favorite Coin: {fav_coin}")
    print(f"Uses: {', '.join(uses)}")

    return "Complete"

if __name__ == '__main__':
    app.run(debug=True)