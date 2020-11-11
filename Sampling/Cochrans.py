from Calculator.Square import squaring
import scipy.stats
from math import ceil

def cochrans(conf, prop):

    z_critical = z_critical = scipy.stats.norm.ppf(1 - (1 - conf) / 2)
    z_critical_squared = squaring(z_critical)

    e = (1-conf)
    e_squared = squaring(e)
    cochrans_n = ceil((z_critical_squared * prop * (1-prop)) / e_squared)

    return cochrans_n



