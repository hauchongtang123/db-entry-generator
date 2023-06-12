import random

def generate_random_days() -> list:
    num_days = random.randint(1, 5)
    whitelist = random.sample(range(7), k=num_days)
    return whitelist