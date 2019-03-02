def multiplication_table(row, col):
    arr = []
   
    for r in range(1, row + 1):
        currentArr = []
        for c in range(1, col + 1):
            currentArr.append(r * c)
        arr.append(currentArr)
    
    return arr
