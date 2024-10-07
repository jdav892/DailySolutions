function insertDash(num){
    let newNum = num.toString()
    let result = ''
    for(let i = 0; i < newNum.length; i++){
            result += newNum[i]
        if(i < newNum[i - 1] && newNum[i] % 2 !== 0 && newNum[i + 1] % 2 !== 0){
            result += '-'
        }
    }
    return result 
}