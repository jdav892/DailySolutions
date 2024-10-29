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
        
        for c in s:
            if c in braceMap:
                if stack and stack[-1] == braceMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    
#O(n)