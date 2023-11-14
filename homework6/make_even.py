def make_even(xs):
   
    l = len(xs)
    g = 0
   
    while g <= l - 1:
        k = xs[g]
        
        if k % 2 != 0:
            xs[g] -= 1
        
        g += 1
    
    return None