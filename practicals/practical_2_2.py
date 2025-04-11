import time
import json

chain = []
new_transaction = []

nonce = 123
previous_block_hash = 'genesis'
hash = 'block1'
new_block = {
    'index': len(chain) + 1,
    'timestamp': int(time.time() * 1000),
    'transaction': new_transaction,
    'nonce': nonce,
    'hash': hash,
    'previous_block_hash': previous_block_hash
}
chain.append(new_block)
new_transaction.clear()

no_of_blocks = int(input("Enter No of Blocks: "))

for _ in range(no_of_blocks):
    transactions = int(input("Enter No of Transactions: "))
    nonce = input("Enter Nonce: ")
    hash = input("Enter hash: ")
    previous_block_hash = chain[-1]['hash']

    for _ in range(transactions):
        amount = input("Enter amount: ")
        sender = input("Enter sender: ")
        recipient = input("Enter recipient: ")
        new_transaction.append({
            'amount': amount,
            'sender': sender,
            'recipient': recipient
        })

    new_block = {
        'index': len(chain) + 1,
        'timestamp': int(time.time() * 1000),
        'transaction': new_transaction,
        'nonce': nonce,
        'hash': hash,
        'previous_block_hash': previous_block_hash
    }
    chain.append(new_block)
    new_transaction.clear()

print(json.dumps(chain, indent=2))