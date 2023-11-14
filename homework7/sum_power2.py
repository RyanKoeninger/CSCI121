def sum_power2(x):
    if x == 0:
        return '1'
    else:
        return ('(' + sum_power2(x - 1) + '+' + sum_power2(x - 1) + ')')