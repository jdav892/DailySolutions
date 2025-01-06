class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        
        for left, right, d in shifts:
            prefix[right + 1] += 1 if d else -1
            prefix[left] += -1 if d else 1
            
            
        diff = 0
        result = [ord(char) - ord("a") for char in s]
        
        for i in reversed(range(len(s) + 1)):
            diff += prefix[i]
            result[i - 1] = (diff + result[i - 1]) % 26
            
        s = [chr(ord("a") + n) for n in result]
        
        return "".join(s)