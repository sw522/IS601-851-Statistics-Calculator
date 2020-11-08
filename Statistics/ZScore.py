from Statistics.Mean import mean
from Statistics.StandardDeviation import stddev


def zscore(a):
    zmean = mean(a)
    sd = stddev(a)
    zlist = []
    for x in a:
        z = round(((x - zmean) / sd), 6)
        zlist.append(z)
    return zlist

