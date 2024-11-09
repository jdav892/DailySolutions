def filter_long_words(sentence, n):
    words = sentence.split()
    result = []
    for word in words:
        if len(word) > n:
            result.append(word)
    return result