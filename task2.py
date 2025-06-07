import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash=''):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = ""

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        print("Mining block...")
        start_time = time.time()
        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith(prefix):
                break
            self.nonce += 1
        end_time = time.time()
        print(f"Block mined: {self.hash}")
        print(f"Nonce: {self.nonce}")
        print(f"Time taken: {round(end_time - start_time, 2)}s")

# Test mining
block = Block(1, "Some transaction data")
block.mine_block(difficulty=4)
