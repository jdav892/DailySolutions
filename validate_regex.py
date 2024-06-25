import re
def validate_code(code):
    check_code = re.search("^[123]", code)
    if check_code:
        return True
    else:
        return False