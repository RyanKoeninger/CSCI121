def average(f,start,end):
    
    i = start
    a = 0

    while i <= end:
        b = f(i)
        a += b
        i += 1
    
    ret = a / (end - start + 1)

    return ret
