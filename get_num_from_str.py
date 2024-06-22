def get_number_from_string(st):
    st1 = int("".join(c for c in st if c.isnumeric()))
    return st1