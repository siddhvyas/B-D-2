import time

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

for _ in range(3):
    nonce = input("Enter Nonce: ")
    hash = input("Enter hash: ")
    previous_block_hash = chain[-1]['hash']

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

print(chain)
