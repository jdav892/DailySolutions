class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        forms = {"".join(sorted(str(1 << n))) for i in range(31)}
        
        return "".join(sorted(str(n))) in forms