#def sort_my_string(s):
#    even = ""
#    odd = ""
#    for i in range(len(s)):
#        if i % 2 == 0:
#            even += i
#        else:
#            odd += i
#    return f"{even} {odd}"


def sort_my_string(s):
    return f"{s[0::2]} {s[1::2]}"