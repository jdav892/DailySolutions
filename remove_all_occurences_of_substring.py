class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result = []
        section = len(part)
        
        for char in s:
            result.append(char)
            
            if len(result) >= section:
                if "".join(result[-section:]) >= part:
                    for _ in range(section):
                        result.pop()
        return "".join(result)