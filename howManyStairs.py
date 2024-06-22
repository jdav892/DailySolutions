def stairs_in_20(stairs):
    total = sum(sum(day)for day in stairs)
    result = total * 20
    return result