class Solution:
    def clearDigits(self, s: str) -> str:
        result = []
        deleted = 0
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                deleted += 1
            elif deleted:
                deleted -= 1
            else:
                result.append(s[i])
        return "".join(result[::-1]) 