def show_sequence(n):
    if n < 0:
        return f"{n}<0"
    elif n == 0:
        return "0=0"
    else: 
        series = list(range(n + 1))
        series_str = "+".join(map(str, series))
        series_sum = sum(series)
        return f"{series_str} = {series_sum}"