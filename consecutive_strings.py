def longest_consec(strarr, k):
    result = ""
    if len(strarr) < k or k <= 0:
        return ""
    for i in range(len(strarr)):
        combo = "".join(strarr[i:i + k])
        if len(combo) > len(result):
            result = combo
    return result

