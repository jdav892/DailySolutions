class Solution:
    def minMaxDifference(self, num: int) -> int:
        INF = 10 ** 20
        
        mx = 0
        mn = INF
        
        str_num = str(num)
        
        for start in range(0, 10):
            for end in range(0, 10):
                if start != end:
                    x = int(str_num.replace(str(start), str(end)))
                    mx = max(x, mx)
                    mn = min(x, mn)
                    
        return mx - mn