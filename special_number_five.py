def special_number(number):
    specials = [0 ,1 ,2, 3, 4, 5]
    nums = [int(num) for num in str(number)]
    for digit in nums:
        if digit not in specials:
            return "NOT!!"
    return "Special!!"

#return "Special!!" if max(str(n)) <= "5" else "NOT!!"