class Solution:
    def countLargestGroup(self, n: int) -> int:
        map = defaultdict(int)
        for x in range(1, n + 1):
            s = str(x)
            sum = 0
            for y in s:
                sum += int(y)
            map[sum] += 1
        
        change = -1
        result = 0
        for k in map:
            if map[k] > change:
                change = map[k]
                result = 1
            elif map[k] == change:
                result += 1
        return result