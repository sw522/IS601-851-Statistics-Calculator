import random
from operator import itemgetter
from Generator.RandomNumber import randomnumber
from Generator.RandomListSeed import randomlistseed

def randomitemsseed(a, n, seed):
    b = randomlistseed(0, len(a) -1 , n, seed)
    return list(itemgetter(*b)(a))