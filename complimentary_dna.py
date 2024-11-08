def DNA_strand(dna):
    result = ""
    for char in dna:
        if char == "A":
            result += "T"
        elif char == "T":
            result += "A"
        elif char == "C":
            result += "G"
        elif char == "G":
            result += "C"
    return result

def new_dna(strand):
    ref = {
        "A" : "T",
        "T" : "A",
        "C" : "G",
        "G" : "C"
    }
    
    return ''.join([ref[l] for l in strand])