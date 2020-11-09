import random
from Generator.RandomNumber import randomnumber

def randitem(a):
    b = randomnumber(0, len(a) - 1)
    return a[b]