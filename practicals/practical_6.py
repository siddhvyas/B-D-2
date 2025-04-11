from flask import Flask, request, jsonify
import hashlib
import base58

app = Flask(__name__)

# Generate Brain wallet from username
def generate_brain_wallet(username):
    # Use SHA256 hash of username to simulate brain wallet
    sha256_hash = hashlib.sha256(username.encode('utf-8')).digest()
    private_key = sha256_hash  # You can use it as private key
    public_key = sha256_hash  # In a real Bitcoin implementation, you would need to calculate the public key
    # For the sake of simplicity, we're skipping some steps here
    address = base58.b58encode(sha256_hash).decode('utf-8')  # Using Base58 to encode it into address (simplified for demo)
    private_key_hex = private_key.hex()
    return address, private_key_hex

@app.route('/')
def index():
    return "Welcome to the Brain Wallet Generator"

@app.route('/wallet', methods=['POST'])
def wallet():
    if request.is_json:
        data = request.get_json()
        username = data.get('username')

        # Generate wallet address and private key
        addr, pk = generate_brain_wallet(username)

        # Return the result as JSON
        return jsonify({
            "username": username,
            "address": addr,
            "private_key": pk
        })

if __name__ == '__main__':
    app.run(debug=True, port=7000)