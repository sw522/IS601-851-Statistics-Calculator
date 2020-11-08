from Calculator.Division import division


def mean(a):
    try:
        n = len(a)
        total = sum(a)
        return division(total, n)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")