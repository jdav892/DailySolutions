def paint_letter_boxes(start, finish):
    result = [0] * 10
    for num in range(start, finish + 1):
        for digit in str(num):
            result[int(digit)] += 1
    return result