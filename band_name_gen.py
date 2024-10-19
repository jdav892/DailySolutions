def band_name_generator(name):
    if name[-1] == name[0]:
        return name[:-1].capitalize() + name[0:]
    else:
        return f"The {name.capitalize()}"