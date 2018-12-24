import math


def expanded_form(num):
    i = 0

    while math.floor(num / (10 ** i)) > 10:
        i += 1
        
    prev = 0
    string = ''
    digits = []

    for j in range(i, -1, -1):
        num -= prev
        n = math.floor((num) / (10 ** j)) * (10 ** j)
        prev = n

        if n != 0:
            digits.append(str(n))
            
    return ' + '.join(digits)
