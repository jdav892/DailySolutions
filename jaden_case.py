def to_jaden_case(string):
    words = string.split()
    jaden = [word.capitalize() if "'" not in word else word[0].upper() + word [1:] for word in words]
    return ' '.join(jaden)