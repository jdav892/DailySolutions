def count_letters_and_digits(s):
    count = 0
    for char in s:
        if char.isalnum():
            count += 1
    return count

#return sum(map(str.isalnum, s))