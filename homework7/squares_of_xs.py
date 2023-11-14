def squares_of(xs):

    length = len(xs)
    retLis = []
    y = 0

    while y < length:
        z = xs(y)
        retLis.append(z)
        y += 1
    
    return retLis