def array_leaders(numbers):
    leaders = []
    for i, num in enumerate(numbers):
        if num > sum(numbers[i + 1:]):
            leaders.append(num)
    return leaders

