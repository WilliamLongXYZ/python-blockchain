import datetime
import hashlib
import os
from socket import gethostbyname, gethostname


class Block:
    def __init__(self):
        self.timestamp = datetime.datetime.now()
        self.nonce = 0
        self.data = "Genesis"
        self.previous_hash = 0x0
        self.node_number_formatted = 0000
        self.node_ip = gethostbyname(gethostname())
        self.block_num = 0
        self.key = os.environ['crypt-key']
        self.hash = self.hash()
        self.block_num = 0
        self.data = "Gensis"
        self.nonce = 0

    def __repr__(self):
        return (f"Block Hash: {str(self.hash)}\n"
                f"Block #: {self.block_num}\n"
                f"Block Data: {self.data}\n"
                f"Mined From Node: {self.node_number_formatted}\n"
                f"Mined: {self.timestamp}\n"
                f"Hashes: {self.nonce}\n")

    def hash(self):
        h = hashlib.sha512()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.node_number_formatted).encode('utf-8') +
        str(self.node_ip).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.block_num).encode('utf-8') +
        str(self.key).encode('utf-8')
        )
        return h.hexdigest()


def main():
    with open("blockchain.raw", 'a') as rawstore:
        rawstore.write(f"{Block()}\n")

main()
