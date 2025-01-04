class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set()
        start = set()
        end = Counter(s)
        
        for middle in s:
            end[middle] -= 1
            
            for char in start:
                if end[char] > 0:
                    result.add((middle, char))
            start.add(middle)
            
        return len(result)