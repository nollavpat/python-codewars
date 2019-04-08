def valid_parentheses(string):
    open_paren = 0
    close_paren = 0
    preArray = []
    postArray = []

    OPEN_PAREN = "("
    CLOSE_PAREN = ")"

    for i in string:
        if i == OPEN_PAREN:
            open_paren += 1
        elif i == CLOSE_PAREN:
            close_paren += 1

        if i == OPEN_PAREN or i == CLOSE_PAREN:
            preArray.append(i)

    if open_paren != close_paren:
        return False

    for i in preArray:
        if i == OPEN_PAREN:
            postArray.append(i)
        if i == CLOSE_PAREN and len(postArray) > 0:
            postArray.pop()

    if len(postArray) != 0:
        return False

    return True


print(valid_parentheses("hi())("))
