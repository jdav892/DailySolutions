def initialize_names(name):
    names = name.split(" ")
    new_name = []
    for i in range(len(names)):
        if names[i] != names[0] and names[i] != names[-1]:
            char = f"{names[i][0]}."
            new_name.append(char)
        else:
            new_name.append(names[i])
            
    return " ".join(new_name)