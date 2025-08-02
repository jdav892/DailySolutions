class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        N = len(nums)
        
        seen = set()
        result = set()
        
        def fun(index, current):
            if index >= N:
                result.add(current)
                return
            if (index, current) in seen:
                return

            seen.add((index, current))
            result.add(current)
            
            fun(index + 1, current | arr[index])
            
        for i in range(N):
            fun(i, arr[i])
        return len(result)