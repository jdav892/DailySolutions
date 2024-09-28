def seven_ate_9(str_):
    num_str = list(num_str)
    
    num = 0
    while num < len(str_) - 2:
        if num_str[num] == '7' and num_str[num + 1] == '9' and num_str[num + 2]:
            del num_str[num + 1]
        else:
            num += 1
    return ''.join(num_str)

#while "797" in str:
#   str_ = str_.replace("797", "77")
#return str_