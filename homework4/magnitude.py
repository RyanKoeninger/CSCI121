from re import A


def magnitude(num):
   
    x = 0

    if num == 0:
        return 0
    elif (num == 1):
        return 1
    elif num > 1:
        while (num > 0):
            num = num // 2
            x = x + 1
        return x