def max_gap(numbers):
    sorted_nums = sorted(numbers)
    gap = [sorted_nums[i + 1] - sorted_nums[i] for i in range(len(sorted_nums) - 1)]
    return max(gap)