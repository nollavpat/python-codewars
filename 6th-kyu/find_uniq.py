def find_uniq(arr):
    first_element = arr[0]
    second_element = arr[1]
    third_element = arr[2]

    n = first_element

    if first_element == second_element:
        for i in range(1, len(arr)):
            if arr[i] != n:
                n = arr[i]
                break

    return n

    if first_element != second_element:
        if first_element == third_element:
            return second_element
        else:
            return first_element
