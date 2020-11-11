from Generator.Generator import Generator
from Sampling.SimpleRandomSampling import simplerandomsampling
from Sampling.SimpleRandomSamplingSeed import simplerandomsamplingseed
from Sampling.ConfidenceInterval import confidenceinterval
from Sampling.MarginOfError import marginoferror
from Sampling.Cochrans import cochrans
from Sampling.FindSampleSize import findsamplesize
import pprint

class Sampling(Generator):

    data = []

    def __init__(self):
        super().__init__()

    def srs(self, data, n):
        self.result = simplerandomsampling(data, n)
        return self.result

    def srsseed(self, data, n, seed):
        self.result = simplerandomsamplingseed(data, n, seed)
        return self.result

    def moe(self, data, conf):
        self.result = marginoferror(data, conf)
        return self.result

    def conf_int(self, data, conf):
        self.result = confidenceinterval(data, conf)
        return self.result

    def cochrans_n(self, conf, prop):
        self.result = cochrans(conf, prop)
        return self.result

    def find_n(self, conf, width):
        self.result = findsamplesize(conf, width)
        return self.result