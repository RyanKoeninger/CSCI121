def primes_list(n):

    primes = []
    x = 2
    l = 0
    m = 0

    while len(primes) < n:

        y = x - 1

        while y > 1:
            
            l = x % y
            if l == 0:
                m += 1
            y -= 1
        
        if m == 0:
            primes.append(x)
        
        x += 1
        l = 0
        m = 0
    
    return primes
            
            




            
