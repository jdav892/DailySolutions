def alphabet_position(text):
    positions = [str(ord(char.lower()) - ord('a') + 1) for char in text if char.isalpha()]
    return ' '.join(positions)