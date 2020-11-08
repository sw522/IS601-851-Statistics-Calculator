from collections import Counter

def mode(a):
    try:
        n = len(a)
        count = Counter(a)
        get_mode = dict(count)
        mode = [k for k, v in get_mode.items() if v == max(list(count.values()))]
        if len(mode) == n:
            get_mode = "No mode found"
        else:
            get_mode = mode[0]
        return get_mode
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")