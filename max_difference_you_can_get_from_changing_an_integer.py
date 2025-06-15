class Solution:
    def maxDiff(self, num: int) -> int:
        
        INF = 10 ** 20

        mx = 0
        mn = INF

        str_num = str(num)

        for start in range(0, 10):
            for end in range(0, 10):
                if start != end:
                    sx = str_num.replace(str(start), str(end))
                    if sx[0] == "0":
                        continue
                    x = int(sx)

                    mx = max(x, mx)
                    mn = min(x, mn)

        return mx - mn