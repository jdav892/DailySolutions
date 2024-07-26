def calc(x):
    total1 = "".join(str(ord(c)) for c in x)
    total2 = total1.replace("7", "1")
    
    total1_ascii = sum(int(digit) for digit in total1)
    total2_ascii = sum(int(digit) for digit in total2)
    
    return total1_ascii - total2_ascii