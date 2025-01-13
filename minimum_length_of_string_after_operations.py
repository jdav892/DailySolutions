class Solution:
    def minimumLength(self, s: str) -> int:
        count = 0
        
        for c in Counter(s).values():
            if c % 2 == 1:
                count += 1
            else:
                count += 2
        return count