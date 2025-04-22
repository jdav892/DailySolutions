class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        f = collections.Counter(answers)
        
        result = 0
        for key in f.keys():
            result += ((f[key] + key) // (key + 1) * (key + 1))
        return result