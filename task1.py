import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def __str__(self):
        return f"Block {self.index}:\nData: {self.data}\nHash: {self.hash}\nPrevHash: {self.previous_hash}\n"

# Create and link blocks
block0 = Block(0, time.time(), "Genesis Block")
block1 = Block(1, time.time(), "Second Block", block0.hash)
block2 = Block(2, time.time(), "Third Block", block1.hash)

# Print blocks
print(block0)
print(block1)
print(block2)

# Tampering
block1.data = "Tampered Data"
block1.hash = block1.calculate_hash()
print("\nAfter tampering Block 1:")
print(block1)
print(block2)  # Still refers to old hash of block1 — chain is now broken
