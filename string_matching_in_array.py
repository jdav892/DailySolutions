class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matches = []
        
        newStr = " ".join(words)
        
        for word in words:
            if newStr.count(word) > 1:
                matches.append(word)
        return matches