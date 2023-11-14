def replace_using(s,d):
    
    sentence = s.split(' ')
    k = 0
    
    while k < len(sentence):
        w = sentence[k]

        if w in d:
            
            sentence[k] = d[w]
        
        k += 1
    
    ret = ' '.join(sentence)

    return ret