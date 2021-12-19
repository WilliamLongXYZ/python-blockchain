import datetime
import hashlib
import os
import socket
import time


node_number_formatted = format(0000, "04b")
node_ip = socket.gethostbyname(socket.gethostname())

def mine(previous, transactions, timestamp, block_num):
        difficulty = 16
        max_nonce = 2**difficulty
        target = 2**(512 - difficulty)
        nonce = 0
        for _ in range(max_nonce):
                if int(create_block(get_hash_itself(previous), nonce, transactions, timestamp, block_num, 1)[-1], 16) <= target:
                        return create_block(get_hash_itself(previous), nonce, transactions, timestamp, block_num)
                else: nonce += 1
        return create_block(get_hash_itself(previous),0, transactions, timestamp, block_num)

def get_parent_hash(block):
        return block[0]

def get_nonce(block):
        return block[1]
        
def get_transactions(block):
        return block[2]

def get_node_number(block):
        return block[3]

def get_timestamp(block):
        return block[4]

def get_block_num(block):
        return block[5]

def get_hash_itself(block):
        return block[6]


def print_block(block, timestamp, block_num):
        return (f"Previous Hash: {get_parent_hash(block)}\n"
                f"Transactions: {get_transactions(block)}\n"
                f"Mined From Node: {node_number_formatted}\n"
                f"Node IP: {node_ip}\n"
                f"Mined: {timestamp}\n"
                f"Block #: {block_num}\n"
                f"Block Hash: {get_hash_itself(block)}\n"
                f"Hashes: {get_nonce(block)}\n"
                )

def create_block(parent_hash, nonce, transactions, timestamp, block_num, only_hash=False):
        hash_itself = hashlib.sha512()
        hash_itself.update(
                str(parent_hash).encode('utf-8') +
                str(nonce).encode('utf-8') +
                str(transactions).encode('utf-8') +
                str(node_number_formatted).encode('utf-8') +
                str(node_ip).encode('utf-8') +
                str(timestamp).encode('utf-8') +
                str(block_num).encode('utf-8')
        )
        if only_hash: return hash_itself.hexdigest()
        return (parent_hash, nonce, transactions, node_number_formatted, timestamp, block_num, hash_itself.hexdigest())

def create_genesis_block(transactions):
        return create_block(0, 0, transactions, time.time(), 0)

def write_block(current_block):
        with open("blockchain.raw", "a") as rawstore:
                rawstore.write()

def read_block():
        with open("blockchain.raw", "r") as raw: lines = raw.readlines()
        self_hash = lines[-3].split(' ')[-1].replace('\n', '')
        block_num = int(lines[-4].split(' ')[-1].replace('\n', ''))
        return (self_hash, block_num)

def main():
        # if there is no blockchain file, create it, and make a genesis block
        if not os.path.exists("blockchain.raw"):
                current = create_genesis_block(None)
                block_num = 0
                current_block = print_block(current, get_timestamp(current), block_num)
                with open("blockchain.raw", mode='a') as raw: raw.write(f"{current_block}\n")
        else:
                self_hash, block_num = read_block()
                current = (None, None, None, None, None, block_num, self_hash)
        while 1:
        # for i in range(8):
                timestamp = time.time()
                previous = current
                block_num += 1
                current = mine(previous, None, timestamp, block_num)
                current_block = print_block(current, timestamp, block_num)
                nonce = get_nonce(current)
                transactions = get_transactions(current)
                with open("blockchain.raw", mode='a') as raw: raw.write(f"{current_block}\n")

if __name__ == "__main__":
        main()
