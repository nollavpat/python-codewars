def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []

    def is_positive(n):
        return n > 0

    def is_negative(n):
        return n < 0
    
    positive_numbers = list(filter(is_positive, arr))
    negative_numbers = list(filter(is_negative, arr))

    return [len(positive_numbers), sum(negative_numbers)]

print(count_positives_sum_negatives([]))