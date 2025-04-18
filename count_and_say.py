class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        current = "1"
        for i in range(n-1):
            new = []
            obs = False
            count = 0
            for j in range(len(current)):
                if obs:
                    if current[j] == observing:
                        count += 1
                    else:
                        new.append(f'{count}{observing}')
                        observing = current[j]
                        count = 1
                else:
                    count = 1
                    observing = current[j]
                    obs = True
            new.append(f'{count}{observing}')
            current = ''.join(new)
        return current