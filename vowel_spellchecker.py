class Solution:
    def spellchecker(self, wordList: List[str], queries: List[str]) -> List[str]:
        seen = set(wordList)
        caps = {}
        vowels = {}
        
        def norm(w):
            result = []
            for c in w.lower():
                if c in "aeiou":
                    result.append("w")
                else:
                    result.append(c)
            return "".join(result)
        
        for word in reversed(wordList):
            caps[word.lower()] = word
            vowels[norm(word)] = word
            
        result = []
        for q in queries:
            if q in seen:
                result.append(q)
                continue
            
            if q.lower() in caps:
                result.append(caps[q.lower()])
                continue
        
            vow = norm(q)
            if vow in vowels:
                result.append(vowels[vow])
                continue
            
            result.append("")
        return result 