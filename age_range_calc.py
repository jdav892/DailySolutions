import math
def dating_range(age):
    if age <= 14:
        min_age = age - .10 * age
        max_age = age + .10 * age
    else:
        min_age = (age / 2) + 7
        max_age = (age - 7) * 2
    return f"{math.floor(min_age)}-{math.floor(max_age)}"
