class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        #if len(s) % 2 == 1:
        #    return False
        #
        #stack_locked = [] 
        #stack_unlocked = []
        #
        #for i in range(len(s)):
        #    if locked[i] == "0":
        #        stack_unlocked.append(i)
        #    elif s[i] == "(":
        #        stack_locked.append(i)
        #    else:
        #        if stack_locked:
        #            stack_locked.pop()
        #        elif stack_unlocked:
        #            stack_unlocked.pop()
        #        else:
        #            return False
        #
        #while stack_locked and stack_unlocked and stack_locked[-1] < stack_unlocked[-1]:
        #    stack_locked.pop()
        #    stack_unlocked.pop()
        #if stack_locked:
        #    return False
        #
        #return True
        if len(s) % 2 == 1:
            return False
        
        locked_count = 0
        unlocked_count = 0
        
        for i in range(len(s)):
            if locked[i] == "0":
                unlocked_count += 1
            elif s[i] == "(":
                locked_count += 1
            else:
                if locked_count:
                    locked_count -= 1
                elif unlocked_count:
                    unlocked_count -= 1
                else:
                    return False
                
        if locked_count == 0:
            return True
        
        locked_count = 0
        unlocked_count = 0
        
        for i in reversed(range(len(s))):
            if locked[i] == "0":
                unlocked_count += 1
            elif s[i] == ")":
                locked_count += 1
            else:
                if locked_count:
                    locked_count -= 1
                elif unlocked_count:
                    unlocked_count -= 1
                else:
                    return False
        
        return True    
            
                
        
                