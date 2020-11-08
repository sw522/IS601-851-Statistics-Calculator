from Sampling.MarginOfError import marginoferror
from Calculator.SquareRoot import squarerooting
import scipy.stats
from math import ceil

def cochrans(a, conf, prop):

    z_critical = z_critical = scipy.stats.norm.ppf(1 - (1 - conf) / 2)
    z_critical_squared = squarerooting(z_critical)

    moe = marginoferror(a,conf)
    moe_squared = squarerooting(moe)
    cochrans_n = ceil((z_critical_squared * prop * (1-prop)) / moe_squared)
    return cochrans_n



