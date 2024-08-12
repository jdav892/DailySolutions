def capitals(word):
    order = []
    for index, char in enumerate(word):
        if char.isupper():
            order.append(index)
    return order
        