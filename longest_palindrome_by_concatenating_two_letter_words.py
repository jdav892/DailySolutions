class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        letters = collections.Counter(words)
        count = 0
        extra = 0
        
        for k in letters.keys():
            if k[0] == k[1]:
                if letters[k] % 2 == 1:
                    extra = 1
                count += (letters[k] // 2) * 4
            else:
                new_k = k[1] + k[0]
                count += min(letters[k], letters[new_k]) * 2
        return count + extra * 2