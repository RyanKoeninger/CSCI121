def counts(n,xs):

    l = []
    i = 0

    while len(l) < n:
        l.append(0)

    while i < len(xs):
        l[xs[i]] += 1
        i += 1

    return l


