class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        prev = -1
        for word, group in zip(words, groups):
            if group != prev:
                result.append(word)
                prev = group
        return result