def array_diff(a, b):
    def not_in_b(n):
        return n not in b

    return list(filter(not_in_b, a))