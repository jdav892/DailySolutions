def explode(s):
    combo = ''
    for num in s:
        if num == '0':
            continue
        combo += num * int(num)
    return combo
        