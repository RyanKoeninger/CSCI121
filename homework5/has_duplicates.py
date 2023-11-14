def has_duplicates(xs):

    l = len(xs)
    x = 0
    y = 0

    while x < l:

        z = y + 1

        while z < l:

            j = xs[y]
            k = xs[z]

            if j == k:
                return True
            
            z += 1
        
        y += 1
        x += 1
        
    return False
            
        

