class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matches = []
        
        newStr = " ".join(words)
        
        for word in words:
            if newStr.count(word) > 1:
                matches.append(word)
        return matches
    
    
    
    #for i in range(len(words)):
    #    for j in range(len(words)):
    #        if i == j:
    #            continue
    #        
    #        if word[i] in word[j]:
    #            matches.append(word[i])
    #            
    #return matches
            
        