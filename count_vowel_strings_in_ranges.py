class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        
        prefix = [0] * (len(words) + 1)
        
        vowel = 0
        
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                vowel += 1
                prefix[i + 1] = vowel
            
        result = [0] * len(queries)
        
        for i, query in enumerate(queries):
            l, r = query
            result[i] = prefix[r + 1] - prefix[l]
        return result