class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        braceMap = {
            ")" : "(", 
            "}" : "{",
            "]" : "["
        }
        
        openingBrackets = ['(', '{', '[']
        closingBrackets = [')', '}', ']']
        
        for char in s:
            if char in openingBrackets:
                stack.append(char)
            elif char in closingBrackets:
                if len(stack) == 0 or stack.pop() != braceMap[char]:
                    return False
        return len(stack) == 0
    
