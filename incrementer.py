def incrementer(nums):
    new_list = []
    for index in range(len(nums)):
        increment = nums[index] + (index + 1)
        single_digits = increment % 10
        new_list.append(single_digits)
    return new_list

# return [ (v + i ) % 10 for i, v in enumerate(nums, 1)]