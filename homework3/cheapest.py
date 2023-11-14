def cheapest(x):
    if x % 14 >= 1:
        bobP = ((x // 14) + 1) * 250  
    else: 
        bobP = (x // 14) * 250
    if x % 11 >= 1:
        aliceP = ((x // 11) + 1) * 200
    else: 
        aliceP = (x // 11) * 200
    if aliceP <= bobP:
        return "Alice"
    else:
        return "Bob"
