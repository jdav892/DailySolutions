def remove_rotten(bag_of_fruits):
    if not bag_of_fruits:
        return []
    
    clean_fruits = []
    for fruit in bag_of_fruits:
        if fruit.startswith("rotten"):
            clean_fruits.append(fruit[6:].lower())
        else:
            clean_fruits.append(fruit.lower())
    return clean_fruits