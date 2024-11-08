def race(v1, v2, g):
    if v2 <= v1:
        return None
    
    speed_diff = v2 - v1
    time = (g / speed_diff) * 3600
    hours = time // 3600
    minutes = (time - hours * 3600) // 60
    seconds = int(time - hours * 3600 - minutes * 60)
    return [hours, minutes, seconds]
    