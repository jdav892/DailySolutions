def html_special_chars(data):
    chars = { "<" : "&lt;", ">" : "&gt;", '"' : "&quot;", "&" : "&amp;"}
    return "".join(chars.join(char, char) for char in data)