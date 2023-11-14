def is_power(x,y):
    if x == y or x == 1:
        return True
    if y > x or y == 1:
        return False
    else:
        return is_power(x / y,y)

    
    