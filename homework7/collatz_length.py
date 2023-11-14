def collatz_length(x):
    if x == 1:
        return 1
    elif x % 2 == 0:
        return 1 + collatz_length(x // 2)
    else:
        return 1 + collatz_length((x * 3) + 1)
    