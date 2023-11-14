def replace_using(s,d):
    
    sentence = s.split(' ')
    k = 0
    
    while k < len(sentence):
        w = sentence[k]

        if w in d:
            w = k[d]
        
        k += 1
    
    return sentence