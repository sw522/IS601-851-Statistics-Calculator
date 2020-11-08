import random

def randomlistseed(a, b, n, seed):
    random.seed(seed)
    return random.sample(range(a, b), n)