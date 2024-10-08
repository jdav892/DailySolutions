function rot13(message){
    let rotStr = ''
    for(let i = 0; i < message.length; i++){
        let char = message[i]
        if(char >= 'a' && char <= 'z'){
            rotStr += String.fromCharCode(((char(0) - 97 + 13) % 26) + 97);
        }else if(char >= 'A' && char <= 'Z'){
            rotStr += String.fromCharCode(((char(0) - 65 + 13) % 26) + 65);
        }else{
            rotStr += char
        } 
    }
    return rotStr
}