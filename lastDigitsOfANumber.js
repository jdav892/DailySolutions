function lastDigit(n, d){
    if(d <= 0){
        return []
    }

    let numArr = []
    let strNum = n.toString()
    for(let i = 0; i < strNum.length; i++){
        numArr.push(strNum[i])
    }
    return numArr.slice(-d)
}