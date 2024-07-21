def to_freud(sentence):
    best_word = "sex"
    words = sentence.split()
    new_words = [best_word for _ in words]
    new = " ".join(new_words)
    return new

# return ' '.join('sex' for _ in sentence.split())
# return (len(s.split()) * "sex ").strip()