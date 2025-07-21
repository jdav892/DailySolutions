class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []

        for char in s:
            result.append(char)
            if len(result) >= 3 and result[-3] == result[-2] == result[-1]:
                result.pop()
        return "".join(result)