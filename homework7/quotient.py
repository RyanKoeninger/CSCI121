def quotient(x,y):

    if x < y:
        return 0
    return 1 + quotient(x-y,y)