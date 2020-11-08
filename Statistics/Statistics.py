from Calculator.Calculator import Calculator
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import stddev
from Statistics.Variance import variance
from Statistics.ZScore import zscore
from Statistics.Mean import mean
from Statistics.SampleStandardDeviation import samplestddev
from Statistics.SampleVariance import samplevariance

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def stddev(self, data):
        self.result = stddev(data)
        return self.result

    def zscore(self, data):
        self.result = zscore(data)
        return self.result

    def sample_variance(self, data):
        self.result = samplevariance(data)
        return self.result

    def sample_stddev(self, data):
        self.result = samplestddev(data)
        return self.result

    pass
