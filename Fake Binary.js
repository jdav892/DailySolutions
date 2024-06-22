function fakeBin(x){
    let result = ''
    for(let i = 0; i < x.length; i++){
        result += x[i] < '5' ? '0' : '1'
    }
    return result
}

//function fakeBin(x){
//    return x.split('').map(digit => digit < '5' ? '0' : '1').join('')
//}