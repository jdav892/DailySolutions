class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        hashmap = {}
        count = 0
        for i, x in enumerate(jewels):
            hashmap[x[i]] = True
        
        for i, y in enumerate(stones):
            if y in hashmap:
                count += 1
        return count
    
# O(n)
#O(n)