def tribonacci(signature, n):
    if n == 0:
        return 0
    
    if n < 3:
        return [signature[i] for i in range(0, n)]
    
    nums = signature[:]
    for i in range(3, n):
        nums.append(nums[i - 1] + nums[i - 2] + nums[i - 3])
    return nums
    