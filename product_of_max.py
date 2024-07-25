def max_product(lst, n_largest_elements):
    if len(lst) < n_largest_elements:
        raise ValueError("The array has fewer elements than the number of elements to combine")
    
    list_sorted = sorted(lst, reverse=True)
    
    product = 1
    for i in range(n_largest_elements):
        product *= list_sorted[i]
        
    return product


#from functools import reduce
#from operator import mul
#from heapq import nlargest
#
#def maxProduct (lst, n):
#    return reduce(mul, nlargest(n, lst))