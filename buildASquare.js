function generateShape(integer){
    let char = '+'
    let shapeStr = []
    for(let i = 0; i < integer; i++){
        shapeStr.push(char.repeat(integer))
    }
    return shapeStr.join('\n')
}

//function generateShape(integer){
//    return("+".repeat(integer) + "\n").repeat(integer).trim()
//}