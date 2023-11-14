def coins(x):
    q = x // 25
    d = x % 25 // 10
    n = x % 25 % 10 // 5
    p = x % 25 % 10 % 5
    tot = q + d + n + p
    return tot
    