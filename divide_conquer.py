def div_con(x):
    reg_int = 0
    str_int = 0
    for number in x:
        if type(number) == int:
            reg_int += number
        elif type(number) == str:
            """Poorly explained question imo"""
            str_int += int(number)
    return reg_int - str_int