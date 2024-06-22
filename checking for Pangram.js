function isPangram(string){
    let alpha ='abcdefghijklmnopqrstuvwxyz'
    let input = string.toLowerCase();
    let count = 0;
    for(let i = 0; i < alpha.length; i++){
        let letter = alpha[i];
        if(input.indexOf(letter) > -1)
        count ++;
    }
    if(count == 26){
        return true
    }else{
        return false
    }
}


// function isPangram(string){
//    return 'abcdefghijklmnopqrstuvwxyz'
//    .split('')
//    .every((x) => string.toLowerCase().includes(x));
//}