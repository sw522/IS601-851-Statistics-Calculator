from Statistics.SampleStandardDeviation import samplestddev
from Calculator.SquareRoot import squarerooting
from Statistics.Mean import mean
from Sampling.MarginOfError import marginoferror
import scipy.stats

def confidenceinterval(a, conf):
    n = len(a)
    m = mean(a)
    sample_stddev = samplestddev(a)
    h = marginoferror(a, conf)

    return round(m,3), round(m-h,3), round(m+h,3)