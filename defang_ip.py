class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        
        new_address = ['[.]' if char == "." else char for char in address]
        
        return new_address
        
        #Simple loop approach
        #for char in address:
        #    if char == ".":
        #        new_address.append('[.]')
        #    else:
        #        new_address.append(char)
        #
        #return new_address
        
        