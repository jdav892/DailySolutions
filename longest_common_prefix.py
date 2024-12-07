class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        
        i = 0
        
        min_len = min(len(first), len(last))
        
        if i < min_len and first[i] == last[i]:
            i += 1
            
        return first[:i] 