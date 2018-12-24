def delete_nth(order, max_e):
    record = {}
    delete_indexes = []

    for i in range(len(order)):
        n = order[i]

        if n not in record.keys():
            record[n] = 0
        else:
            new_n = record.get(n) + 1
            if n in list(map(lambda x: order[x], delete_indexes)):
                delete_indexes.append(i)
            elif new_n == max_e:
                delete_indexes.append(i)
            record[n] = new_n

    for i in list(reversed(delete_indexes)):
        del order[i]

    return order