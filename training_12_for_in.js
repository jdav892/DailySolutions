function giveMeFive(obj){
    let numArr = [];
    for(var key in obj){
        if(key.length == 5){
            numArr.push(key)
        }
        if(typeof obj[key] === 'string' && obj[key].length == 5){
            numArr.push(obj[key])
        }
    }
    return numArr
}