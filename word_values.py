def name_value(my_list):
    def string_value(s):
        return sum(ord(char) - ord('a') + 1 for char in s if char.isalpha())
    result = []
    for i, s in enumerate(my_list):
        value = string_value(s) * (i + 1)
        result.append(value)
    return result
        