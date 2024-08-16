import re
def sum_of_integers_in_string(s):
   numbers = re.findall(r'\d+', s)
   return sum(int(num) for num in numbers)