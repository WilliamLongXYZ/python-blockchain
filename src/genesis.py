import hashlib
import os

block_num = 0
data = "Genesis"
nonce = 0
previous_hash = 0x0

def hash():
    h = hashlib.sha512()
    h.update(
    str(nonce).encode('utf-8') +
    str(data).encode('utf-8') +
    str(previous_hash).encode('utf-8') +
    str(block_num).encode('utf-8') +
    str(key).encode('utf-8')
    )
    return h.hexdigest()

key = os.environ['crypt-key']

class Block:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return (
        f'Block Hash: {str(hash())}\n'
        f'Block #: {block_num}\n'
        f'Block Data: {data}\n'
        f'Hashes: {nonce}\n'
        )

print(Block("Gensis"))
