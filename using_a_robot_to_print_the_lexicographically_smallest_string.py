class Solution:
    def robotWithString(self, s: str) -> str:
        result = []
        best = "a"
        f = collections.Counter(s)
        s = collections.deque(s)
        t = []
        
        while True:
            if len(t) > 0 and t[-1] == best:
                t.pop()
                result.append(best)
                if len(t) > 0:
                    best = min(best, t[-1])
                continue
            if len(s) > 0 and s[0] == best:
                s.popleft()
                f[best] = -1
                result.append(best)
                continue
            if f[best] > 0:
                while s[0] != best:
                    c = s.popleft()
                    f[c] -= 1
                    t.append(c)
                f[best] -= 1
                s.popleft()
                result.append(best)
                continue
            else:
                if best == "z":
                    break
                best = chr(ord(best) + 1)
                
        while len(t) > 0 :
            result.append(t.pop())
        return "".join(result)