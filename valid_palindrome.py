class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = "".join([char for char in s if char.isalnum()]).lower()
        
        return new_str == new_str[::-1]