def contamination(text, char):
    mut_string = ""
    if text == "" or char == "":
        return mut_string
    for i in text:
        mut_string += char
    return mut_string
   
   
#def contamination(text, char):
#return char*len(text) 