function uniTotal(string){
    let chars = 0;
    for(let i = 0; i < string.length; i++){
        let code = string.charCodeAt(i)
        chars += code
    }
    return chars

}