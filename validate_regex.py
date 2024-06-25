import re
def validate_code(code):
    check_code = re.search("^[123]", str(code))
    if check_code:
        return True
    else:
        return False
    
    
# def validcate_code(code):
#   return str(code).startswith(('1', '2', '3'))