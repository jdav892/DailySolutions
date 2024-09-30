def number_of_occurrences(element, sample):
    count = 0
    for el in sample:
        if el == element:
            count += 1
    return count


#return sample.count(element)