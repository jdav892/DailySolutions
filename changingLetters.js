function swap(string){
    let strArr = string.split("")
    for(let i = 0; i < strArr.length; i++){
        if(strArr[i] === "a" || strArr[i] === "e" || strArr[i] === "o" || strArr[i] === "i" || strArr[i] === "u"){
            strArr[i] = strArr[i].toUpperCase()
        }
    }
    return strArr.join("")
}