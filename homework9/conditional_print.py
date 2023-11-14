def conditional_print(f):
    
    def check(x):
        if f(x) == True:
            print(x)
    
    return check