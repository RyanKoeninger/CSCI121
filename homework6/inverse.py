def inverse(d):
   
    e = {}
   
    n = []
    for key in d:
   
        n.append(key)
        if d[key] in e:
            e[d[key]].append(key)
   
        else:
   
            e[d[key]] = n
   
        n = []
   
    return e