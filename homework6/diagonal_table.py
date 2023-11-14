def diagonal_table(x):

    l = []
    a = 0
    
    while len(l) < x:
        lin = [0] * x
        l.append(lin)
    while a < x:
        l[a][a] = 1
        a += 1
    
    return l