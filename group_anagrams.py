from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counter = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            counter[key].append(s)
        
        return list(counter.values())