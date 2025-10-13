class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        
        def is_anagram(a, b):
            return collections.Counter(a) == collections.Counter(b)
        
        
        for word in words:
            if len(result) == 0:
                result.append(word)
                continue
            
            if not is_anagram(result[-1], word):
                result.append(word)
                
        return result