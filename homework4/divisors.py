def divisors(num):

    x = 1
    y = 1
    retStringBeginning = "The divisors of " + str(num) + " are "
    retStringMid = ""
    retStringEnd = "and " + str(num) + "."
    
    if num == 0:
        return "The divisor of 0 is 0"

    elif num == 1:
        return "The divisor of 1 is 1."
    
    else:
        while x < num:
            
            if num % x == 0:
                retStringMid = retStringMid + str(x) + ", "
                y = y + 1 
            x = x + 1
        if y == 2:
            return retStringBeginning + "1 and " + str(num) + "."
        else:
            return str(retStringBeginning) + str(retStringMid) + str(retStringEnd)