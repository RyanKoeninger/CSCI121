from operator import truediv


def perfect_square(num):
    if num >= 0:

        x = 0
        
        while x * x < num:
            x = x + 1
        
        if x * x == num:
            return True
        else:
            return False

    else: 
        return False


