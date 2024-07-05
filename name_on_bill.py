def billboard(name, price=30):
    cost = 0
    for char in name:
        cost += price
    return cost
#other solution would be return(sum(price for letter in name))       