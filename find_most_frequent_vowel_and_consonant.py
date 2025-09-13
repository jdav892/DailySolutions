class Solution:
    def maxFreqSum(self, s: str) -> str:
        s_hash = collections.Counter(s)
        
        v_count = 0
        c_count = 0
        
        for k, v in s_hash.items():
            if k in 'aeiou':
                v_count = max(v_count, v)
            else:
                c_count = max(c_count, v)
                
        return v_count + c_count