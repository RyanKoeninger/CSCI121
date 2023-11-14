def max_of_funcs(f,g):
    
    def highest(x):
        if f(x) > g(x):
            return f(x)
        else:
            return g(x)
    
    return highest