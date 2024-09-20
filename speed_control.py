import math
def gps(s, x):
    if len(x) < 2:
        return 0
    
    max_speed = 0
    for num in range(1, len(x)):
        distance_change = x[num] - x[num - 1]
        speed = (3600 * distance_change) / 2
        max_speed = max(max_speed, speed)
    return math.floor(max_speed)