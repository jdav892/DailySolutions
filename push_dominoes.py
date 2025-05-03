class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        INF = 10**20
        
        def closest(dominoes, direction):
            right = [INF] * N
            for i in range(N):
                if dominoes[i] == direction:
                    right[i] = 0
                elif dominoes[i] == ".":
                    if i - 1 >= 0:
                        right[i] = min(right[i - 1] + 1, INF)
            return right
        
        right = closest(dominoes, "R")
        left = closest(dominoes[::-1], "L")[::-1]
        
        result = [None] * N
        for i in range(N):
            if left[i] < right[i]:
                result[i] = "L"
            elif left[i] > right[i]:
                result [i] = "R"
            else:
                result[i] = "."
        return "".join(result)