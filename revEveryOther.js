function reverse(str){
    let newStr = str.trim().split(/\s+/);
    for(let i = 0; i < newStr.length; i++){
        if(i % 2 !== 0){
            newStr[i] = newStr[i].split("").reverse().join("");
        }
    }
    return newStr.join(" ");
}