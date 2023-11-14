def word_count(x):
    
    words = x.split(' ')

    b = 0
    d = {}

    while b < len(words):
        w = words[b]
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
        b += 1
    
    return d
