class Solution:
    def kthCharacter(self, k: int) -> str:
        s = ["a"]
        
        while len(s) < k:
            nxt = []
            
            for c in s:
                nxt.append(chr((ord('c') - ord('a') + 1) % 26 + ord('a')))

            s.extend(nxt)
        return s[k - 1]