class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        i = 1
        def counter(current):
            result = 0
            neighbor = current + 1
            while current <= n:
                result += min(neighbor, n + 1) - current
                current *= 10
                neighbor *= 10
            return result
        
        while i < k:
            steps = counter(current)
            if i + steps <= k:
                current = current + 1
                i += steps
            else:
                current *= 10
                i += 1
        return current