import datetime
import hashlib


class Block:
    block_num = 1
    next = None
    hash = None
    nonce = 0
    previous_hash = 0xf6837146c8e17306ffc692e36eaeeb581ef04d0d549af66a65fca7257ffab86b4bf0b181dd12b66547c170e1f0771327e8a25903b48d90f61831455e45142409
    timestamp = datetime.datetime.now
    pc_num_for = format(0000, "04b")
    pc_ip = "172.18.0.164"

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha512()
        h.update(
            str(self.nonce).encode('utf-8') + str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.pc_num_for).encode('utf-8') +
            str(self.pc_ip).encode('utf-8') +
            # str(self.timestamp).encode('utf-8') +
            str(self.block_num).encode('utf-8'))
        return h.hexdigest()

    def __repr__(self):
        return (f'Block Hash: {str(self.hash())}\n'
                f'Block #: {self.block_num}\n'
                f'Block Data: {self.data}\n'
                f'Hashes: {self.nonce}\n')


class Blockchain:
    difficulty = 32
    max_nonce = 2**32
    target = 2**(512 - difficulty)
    block = Block(None)
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
        if not self.head:
            self.head = self.block
        while self.head:
            print(self.head)
            self.head = self.head.next


def _main():
    blockchain = Blockchain()
    # mining
    for n in range(5):
        blockchain.mine(Block(f"Block {n+2}"))
        blockchain.show()
    #adding
    blockchain.add(Block('added block'))
    blockchain.show()
    blockchain.add(Block('added block2'))
    blockchain.show()


if __name__ == "__main__":
    _main()
