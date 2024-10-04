def create_dict(keys, values):
    new_dict = {}
    for val in range(len(keys)):
        new_dict[keys[val]] = values[val] if val < len(values) else None
    return  new_dict 