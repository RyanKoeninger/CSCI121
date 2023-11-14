def down_up(x):
    
    list = []
    y = x
    z = 2

    while y > 0:
        list.append(y)
        y = y - 1

    while z <= x:
        list.append(z)
        z = z + 1

    return list
        