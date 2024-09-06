def split_and_merge(string_, separator):
    new_words = string_.split(" ")
    return " ".join([separator.join(list(word)) for word in new_words])