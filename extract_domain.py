import re
def domain_name(url):
    match = re.search(r"(https?://)?(www\.)?([a-zA-Z0-9-]+)\.", url)
    if match:
        return match.group(3)
    return None

    
