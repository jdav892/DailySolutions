class Solution:
    def toLowerCase(self, s: str) -> str:
        new_str = [char.lower() if char == char.upper() else char for char in s]
        
        return "".join(new_str)