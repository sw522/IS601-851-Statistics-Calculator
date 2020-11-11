from Sampling.MarginOfError import marginoferror
from Calculator.SquareRoot import squarerooting
from Calculator.Square import squaring
import scipy.stats
from math import ceil

def findsamplesize(conf, width):

    z_critical = z_critical = scipy.stats.norm.ppf(1 - (1 - conf) / 2)
    z_critical_squared = squarerooting(z_critical)

    moe = width / 2
    p_hat  = .5

    q_hat = 1 - p_hat

    p_times_q = p_hat * q_hat

    z_div_moe = z_critical / moe
    z_div_moe_squared = squaring(z_div_moe)

    n = ceil(p_times_q * z_div_moe_squared)

    return n
