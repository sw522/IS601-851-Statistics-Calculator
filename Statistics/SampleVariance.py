from Calculator.Square import squaring
from Calculator.Division import division
from Statistics.Mean import mean

def samplevariance(a):
    try:
        a_mean = mean(a)
        n = len(a)
        x = 0
        for i in a:
            x = x + squaring(i-a_mean)
        return round(division(x, (n-1)), 7)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")