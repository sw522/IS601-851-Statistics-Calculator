import scipy.stats
from Statistics.SampleStandardDeviation import samplestddev
from Calculator.SquareRoot import squarerooting
from Statistics.Mean import mean

def marginoferror(a, conf):

    n = len(a)
    z_critical = scipy.stats.norm.ppf(1 - (1 - conf) / 2)

    sample_stdev = samplestddev(a)
    se = sample_stdev/squarerooting(n)
    margin_of_error = z_critical * se

    return margin_of_error