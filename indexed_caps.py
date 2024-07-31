def capitalize(s, ind):
    chars = list(s)
    
    for index in ind:
        if 0 <= index < len(chars):
            chars[index] = chars[index].upper()
    
    return ''.join(chars)