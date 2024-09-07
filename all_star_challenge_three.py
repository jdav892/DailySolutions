def remove_vowels(strng):
    vowels = ("a", "e", "i", "o", "u")
    return "".join([l for l in strng if l not in vowels])