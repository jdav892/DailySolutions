class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        stack = []
        
        for x in nums:
            stack.append(x)
            if len(stack) >= 2 and gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                
                l = lcm(a, b)
                stack.append(l)
        return stack