def vaporcode(s):
    new_str = ""
    for char in s:
        if char != " ":
            new_str = f"{char.upper()}  "
    return new_str.split()