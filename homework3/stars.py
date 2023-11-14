def stars(x,y): 
    StarOdd = "* " * (x // 2)
    StarEven = " *" * (x // 2)
    if (x % 2 != 0):
        StarOdd = StarOdd + "*"
        StarEven = StarEven + " "
    if y % 2 == 0:
        s = (str(StarOdd) + "\n" + str(StarEven) + "\n") * (y // 2)
    else:
        s = ((str(StarOdd) + "\n" + str(StarEven) + "\n") * (y // 2)) + str(StarOdd) + "\n"
    return s
    