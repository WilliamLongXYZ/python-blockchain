import datetime
import hashlib
import socket


class Block:
    block_num = 1
    next = None
    hash = None
    nonce = 0
    previous_hash = 0xf6837146c8e17306ffc692e36eaeeb581ef04d0d549af66a65fca7257ffab86b4bf0b181dd12b66547c170e1f0771327e8a25903b48d90f61831455e45142409
    timestamp = datetime.datetime.now()
    node_number_formatted = format(0000, "04b")
    node_ip = socket.gethostbyname(socket.gethostname())

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha512()
        h.update(
            str(self.nonce).encode('utf-8') + str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.node_number_formatted).encode('utf-8') +
            str(self.node_ip).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.block_num).encode('utf-8'))
        return h.hexdigest()

    def __repr__(self):
        return (f"Block Hash: {str(self.hash())}\n"
                f"Block #: {self.block_num}\n"
                f"Block Data: {self.data}\n"
                f"Hashes: {self.nonce}\n")


class Blockchain:
    data = "Data from 1"
    difficulty = 32
    max_nonce = 2**32
    target = 2**(512 - difficulty)
    block = Block(data)
    dummy = head = block

    def add(self, block):
        block.previous_hash = self.block.hash
        block.block_num = self.block.block_num + 1
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for _ in range(self.max_nonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                break
            else:
                block.nonce += 1

    def show(self):
        if not self.head: self.head = self.block
        while self.head:
            print(self.head)
            self.write_block()
            self.head = self.head.next
    def write_block(self):
        with open("blockchain.raw", 'a') as rawstore:
            rawstore.write(f"{self.head}\n")

def mine(blockchain, data):
    blockchain.mine(data)
    blockchain.show()

def read_block():
    pass

def main():
    blockchain = Blockchain()
    # mining
    for n in range(5):
        mine(blockchain, Block(f"Data from {n+1}"))


if __name__ == "__main__":
    main()
