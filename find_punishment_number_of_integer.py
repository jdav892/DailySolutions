class Solution:
    def punishmentNumber(self, n: int) -> int:
        def part(i, cur: int, target: int, string: str):
            if i == len(string) and cur == target:
                return True
            
            for j in range(i, len(string)):
                str[i:j+1]
                if part(j + 1, cur + int(string[i:j+1]), target, string):
                    return True
            return False
        
        result = 0
        for i in range(1, n + 1):
            if part(0, 0, i, str(i*i)):
                result += i * i
        return result