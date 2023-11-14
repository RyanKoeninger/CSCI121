def sum_list_squares(x):

    length = len(x)
    y = 1
    z = 0
    ans = 0

    while y <= length:
        a = x[z]
        b = a ** 2
        ans = ans + b
        y = y + 1
        z = z + 1

    return ans