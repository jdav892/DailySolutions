def valid_spacing(s):
    if s != s.strip():
        return False
    
    words = s.split()
    return " ".join(words) == s