def split_the_bill(x):
    total = sum(x.values())
    average = total/len(x)
    result = {}
    for person, amount in x.items():
        result[person] = round(amount - average, 2)
    return result