class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
         N = len(s)

         seen = set()
         q = collections.deque()
         q.append(s)
         seen.add(s)

         while len(q) > 0:
            current = q.popleft()

            ncurrent = []
            for i in range(N):
                c = current[i]
                if i % 2 == 1:
                    c = str((int(current[i]) + a) % 10)
                ncurrent.append(c)

            nscurrent = "".join(ncurrent)
            if nscurrent not in seen:
                seen.add(nscurrent)
                q.append(nscurrent)

            nscurrent = current[b:] + current[:b]
            if nscurrent not in seen:
                seen.add(nscurrent)
                q.append(nscurrent)
         return list(sorted(seen))[0]

