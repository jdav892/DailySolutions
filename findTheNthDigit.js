var findDigit = function(num, nth){
    let trueNum = Math.abs(num).toString();
    if(nth <=  0){
        return -1
    }

    if(nth > trueNum.length){
        return 0
    }
    return parseInt(trueNum[trueNum.length - nth])

}