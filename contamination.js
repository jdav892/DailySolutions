function contamination(text, char){
    let mutString = ""
    if(!text  || !char){
        return mutString = ""
    }
    for(let i=0; i < text.length; i++){
        mutString += char
    }
    return mutString
}