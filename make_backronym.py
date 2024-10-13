#variable dictionary is preloaded
dictionary = {
    "A": "Able"
}

def make_backronym(acronym):
    return ' '.join(dictionary[char.upper()] for char in acronym)