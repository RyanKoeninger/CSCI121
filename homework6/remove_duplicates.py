def remove_duplicates(xs):
   
    j = 0

    while j <= len(xs) - 1:
        
        k = j + 1
        while k <= len(xs) - 1:
            if xs[j] == xs[k]:
                del xs[k]
            else:
                k += 1
        j += 1
    
    return None