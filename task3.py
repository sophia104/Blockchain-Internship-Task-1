import random

# PoW
miners = {"A": random.randint(10, 100), "B": random.randint(10, 100)}
pow_winner = max(miners, key=miners.get)
print(f"[PoW] Winner: {pow_winner} with power {miners[pow_winner]}")

# PoS
stakers = {"X": random.randint(100, 1000), "Y": random.randint(100, 1000)}
pos_winner = max(stakers, key=stakers.get)
print(f"[PoS] Winner: {pos_winner} with stake {stakers[pos_winner]}")

# DPoS
delegates = ["D1", "D2", "D3"]
votes = {"D1": 2, "D2": 3, "D3": 1}
most_voted = max(votes, key=votes.get)
print(f"[DPoS] Delegate Elected: {most_voted} with {votes[most_voted]} votes")
