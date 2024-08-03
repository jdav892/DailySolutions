def solve(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    num = sum(1 for char in s if char.isdigit())
    special = sum(1 for char in s if not char.isalnum())
    return [upper, lower, num, special]