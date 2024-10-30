def wave(people):
    if people == "":
        return [] 
    else:
        people = people.lower()
        waves = []
        for i, char in enumerate(people):
            if char == " ":
                continue
            else:
                waves.append(people[:i] + people[i].upper() + people[i+1:])
        return waves
            
            
            
        
        
        
    