from Calculator.SquareRoot import squarerooting
from Statistics.SampleVariance import samplevariance

def samplestddev(a):
    try:
        variance = samplevariance(a)
        return round(squarerooting(variance), 5)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")