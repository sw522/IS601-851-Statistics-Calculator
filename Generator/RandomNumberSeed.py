import random

def randomnumberseed(a, b, seed):
    random.seed(seed)
    return random.randint(a, b)