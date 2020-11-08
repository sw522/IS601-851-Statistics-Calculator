from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition


def median(a):
    try:
        n = len(a)
        list_num = [a[i] for i in range(n)]
        list_num.sort()
        if n % 2 == 0:
            median1 = list_num[int(n // 2)]
            median2 = list_num[int(subtraction((n // 2), 1))]
            median_result = division(addition(median1, median2), 2)
        else:
            median_result = list_num[int(division(n, 2))]
        return median_result
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")