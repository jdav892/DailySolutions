import re

def remove(st):
    return re.sub(r'!+$', '', st)


#def remove(st):
#    return st.rstrip('!')
# 