def warn_the_sheep(queue):
    wolf_num =  queue.index("wolf")
    if wolf_num == len(queue) - 1:
        return "Pls go away and stop eating my sheep"
    else:
        dead_sheep = len(queue) - wolf_num - 1
    return f"Oi! Sheep number {dead_sheep}! You are about to be eaten by a wolf!"