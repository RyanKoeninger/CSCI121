def count_palindromes(x):
    
    ct = 0
    rev = ""
    num = 0
    n = 0
    i = n

    while n <= x:
        i = n
        while i != 0:
            num = i % 10
            rev = rev + str(num)
            i = i // 10
            if n == int(rev):
                ct = ct + 1
        n = n + 1
        rev = ""
    return ct + 1