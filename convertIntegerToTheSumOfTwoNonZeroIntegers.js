/**
 * @param {number} n
 * @return {number[]}
 */
var getNoZeroIntegers = function(n) {
    for(let i = 0; i < n; i++){
        let currIndex = i.toString()
        let newNum = n - i
        let newNumStr = newNum.toString()
        if((!currIndex.includes('0')) && (!newNumStr.includes('0'))){
            return [i, newNum]
        }
    }
}