class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (2 **(n - 1))
        
        result = []
        choices = "abc"
        left, right = 1, total
        
        for i in range(n):
            current = left
            partition = (right - left + 1) // len(choices)
            
            for c in choices:
                if k in range(current, current + partition):
                    result.append(c)
                    left = current
                    right = current + partition - 1
                    choices = "abc".replace(c, "")
                current += partition
        return "".join(result)