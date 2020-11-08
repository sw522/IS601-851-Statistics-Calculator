from Generator.RandomNumber import randomnumber
from Generator.RandomNumberSeed import randomnumberseed
from Generator.RandomList import randomlist
from Generator.RandomItem import randitem
from Generator.RandomItemSeed import randitemseed
from Generator.RandomItems import randomitems
from Generator.RandomItemsSeed import randomitemsseed

class Generator:
    def __init__(self):
        pass

    def randnum(self, a, b):
        self.result = randomnumber(a, b)
        return self.result

    def randnum_seed(self, a, b, seed):
        self.result = randomnumberseed(a, b, seed)
        return self.result

    def randlist(self, a, b, n):
        self.result = randomlist(a, b, n)
        return self.result

    def randlist_seed(self, a, b, n, seed):
        self.result = randomlist(a, b, n, seed)
        return self.result

    def randitem(self, a):
        self.result = randitem(a)
        return self.result

    def randitem_seed(self, a, seed):
        self.result = randitemseed(a,seed)
        return self.result

    def randitems(self, a, n):
        self.result = randomitems(a, n)
        return self.result

    def randitems_seed(self, a, n, seed):
        self.result = randomitemsseed(a, n, seed)
        return self.result