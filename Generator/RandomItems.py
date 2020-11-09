import random
from operator import itemgetter
from Generator.RandomNumber import randomnumber
from Generator.RandomList import randomlist
import pprint

def randomitems(a, n):
    b = randomlist(0, len(a) -1, n)
    return list(itemgetter(*b)(a))