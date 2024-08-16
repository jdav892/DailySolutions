def switcheroo(s):
    new_str = ""
    for char in s:
        if char == 'a':
            new_str += 'b'
        elif char == 'b':
            new_str += 'a'
        else:
            new_str += char
    return new_str
