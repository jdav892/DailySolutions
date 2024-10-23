function duplicateEncode(word){
    let obj = {}
    let letter = word.toLowerCase().split("")
    for(let i = 0; i < letter.length; i++){
        let target = letter[i]
        if(obj[target] === undefined){
            obj[target] = 1
        }else{
            obj[target] += 1
        }
    }
    return letter.map((letter) => {
        return obj[target] === 1 ? "(" : ")"
    }).join("")
}

//const duplicateEncoder = (word) => {
//    return word.toLowerCase()
//        .split("")
//        .map((a, i , w) => {
//            return w.indexOf(a) == w.lastIndexOf(a) ? "(" : ")"
//        })
//        .join("")
//}