def solution(n, d):
    if d <= 0:
        return []
    num_str = str(n)
    new_list = [int(num) for num in num_str]
    return new_list[-d:]