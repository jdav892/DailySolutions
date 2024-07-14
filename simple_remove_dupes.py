def solve(arr):
    dupe = set()
    end = []
    for num in reversed(arr):
        if num not in dupe:
            dupe.add(num)
            end.append(num)
    end.reverse()
    return end 