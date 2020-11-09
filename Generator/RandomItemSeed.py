import random
from Generator.RandomNumber import randomnumber

def randitemseed(a, seed):
    random.seed(seed)
    b = randomnumber(0, len(a) - 1)
    return a[b]