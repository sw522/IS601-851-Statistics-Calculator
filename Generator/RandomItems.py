import random
from operator import itemgetter
from Generator.RandomNumber import randomnumber
from Generator.RandomList import randomlist
import pprint

def randomitems(a, n):
    b = randomlist(0, len(a), n)
    #pprint.pprint(list(itemgetter(*b)(a)))
    return list(itemgetter(*b)(a))