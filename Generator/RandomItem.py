import random
from Generator.RandomNumber import randomnumber

def randitem(a):
    b = randomnumber(0, len(a))
    return a[b]