def unique_in_order(iterable):
    unique_list = []
    current_item = None

    for i in iterable:
        if not unique_list:
            current_item = i
            unique_list.append(i)
            continue

        if i not in unique_list:
            unique_list.append(i)
            current_item = i
        elif i in unique_list and current_item != i:
            unique_list.append(i)
            current_item = i

    return unique_list