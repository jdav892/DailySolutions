def am_i_wilson(n):
    known = [5, 13, 563]
    return n in known



#import math
#def another_wilson(n):
#    if n < 2:
#        return False
#    for i in range(2, int(math.sqrt(n)) + 1):
#        if n % i == 0:
#            return False
#    
#    facto = math.factorial(n - 1)
#    expression = facto + 1
#    
#    return expression % (n * n) == 0