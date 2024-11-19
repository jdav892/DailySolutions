def flick_switch(lst):
    new_list = []
    switch = True
    for word in lst:
        if word == "flick":
            switch = not switch
        new_list.append(switch)
    return new_list