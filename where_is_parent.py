def find_children(dancing_brigade):
    parents = []
    children = []
    
    for char in dancing_brigade:
        if char.isupper():
            parents.append(char)
        elif char.islower():
            children.append(char)
            
    parents.sort()
   
   
    line = '' 
    for parent in parents:
        line += parent
        for child in sorted(children):
            if child.upper() == parent:
                line += child
    return line