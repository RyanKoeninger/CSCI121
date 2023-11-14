def remainder(x,y):

    z = x - y
    if x < y:
        return x
    return remainder(z,y)
