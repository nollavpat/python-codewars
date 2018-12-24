def invert(lst):
    def do(number):
        return number * -1

    return list(map(do, lst))