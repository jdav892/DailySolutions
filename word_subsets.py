class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = defaultdict(int)
        
        for char in words2:
            count_char = Counter(char)
            for chars, count_1 in count_char.items():
                count[chars] = max(count[chars], count_1)
                
        
        result = []
        
        for char in words1:
            count_char = Counter(char)
            for chars, count_1 in count.items():
                if count_char[chars] < count_1:
                    flag = False
                    break
        
            if flag:
                result.append(char)
            
        return result