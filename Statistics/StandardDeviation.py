from Calculator.SquareRoot import squarerooting
from Statistics.Variance import variance

def stddev(a):
    try:
        a_variance = variance(a)
        return round(squarerooting(a_variance), 5)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")