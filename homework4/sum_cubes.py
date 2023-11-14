def sum_cubes(x):
    if x <= 0:
        return 0
    else:
        sum = 1
        while x > 1:
            sum = sum + (x * x * x)
            x = x - 1
        return sum
