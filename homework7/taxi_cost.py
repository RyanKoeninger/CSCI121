def taxi_cost(miles):
    if miles <= 10:
        cost = 3 + (2 * miles)
    else: 
        cost = 4 * miles
    return cost