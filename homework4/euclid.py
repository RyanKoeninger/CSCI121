def euclid(x,y):
    
    while x != y:
        
        if y > x:
            y = y - x
        
        if x > y:
            x = x - y
    
    if x == 1 or y == 1:
        return False
        
    else:
        return True

       
        
