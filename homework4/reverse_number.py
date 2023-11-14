def reverse_number(x):
    rev = ""
    num = 0
    
    while (x != 0):
        num = x % 10
        rev = rev + str(num)
        x = x // 10
    return int(rev)