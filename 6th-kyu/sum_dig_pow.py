import functools


def sum_dig_pow(a, b):
    special_numbers = []

    for i in range(a, b + 1):
        i_in_str = str(i)
        i_len = len(i_in_str)
        is_special = False
        total = 0
        k = 1

        for j in range(i_len):
            i_in_int = int(i_in_str[j])
            total += i_in_int ** k
            k += 1

        if total == i:
            special_numbers.append(i)

    return special_numbers