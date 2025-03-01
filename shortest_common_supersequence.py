class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N, M = len(str1), len(str2)
        #bottom up approach
        prev = [str2[j:] for j in range(M)]
        prev.append("")
        
        for i in reversed(range(N)):
            current = [""] * M
            current.append(str1[i:])
            
            for j in reversed(range(M)):
                if str1[i] == str2[j]:
                    current[j] = str1[i] + prev[j + 1]
                else:
                    res1 = str1[i] + prev[j]
                    res2 = str2[j] + current[j + 1]
                    if len(res1) < len(res2):
                        current[j] = res1
                    else:
                        current[j] = res2
            prev = current
        return current[0]
                    