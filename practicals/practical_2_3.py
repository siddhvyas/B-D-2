import time
import json

# Initialize blockchain with a genesis block
blockchain = [{
    'index': 1,
    'timestamp': time.time(),
    'transactions': [],
    'nonce': 123,
    'hash': 'block1',
    'previous_hash': 'genesis',
}]
new_transactions = []

def create_new_block(nonce, previous_hash, hash):
    block = {
        'index': len(blockchain) + 1,
        'timestamp': time.time(),
        'transactions': new_transactions.copy(),
        'nonce': nonce,
        'hash': hash,
        'previous_hash': previous_hash,
    }
    new_transactions.clear()  # Reset the list of new transactions
    blockchain.append(block)
    return block

def create_new_transaction(amount, sender, recipient):
    new_transactions.append({'amount': amount, 'sender': sender, 'recipient': recipient})
    return blockchain[-1]['index'] + 1

def last_block():
    return blockchain[-1]

def previous_hash():
    return last_block()['hash']

# Main script
def main():
    while True:
        print("\n1. Add Transaction")
        print("2. Add Block")
        print("3. View Blockchain")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = input("Enter amount: ")
            sender = input("Enter sender: ")
            recipient = input("Enter recipient: ")
            create_new_transaction(amount, sender, recipient)
            print("Transaction added!")

        elif choice == "2":
            nonce = input("Enter nonce: ")
            hash_value = input("Enter hash: ")
            create_new_block(nonce, previous_hash(), hash_value)
            print("Block added!")

        elif choice == "3":
            print(json.dumps(blockchain, indent=2))

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()