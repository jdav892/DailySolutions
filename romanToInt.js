/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let romansMap = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500, 
        "M": 1000,
    }

    let result = 0
    for(let i = 1; i < s.length; i++){
        if(i + 1 > s.length && romansMap[s[i]] < romansMap[s[i + 1]]){
            result -= romansMap[s[i]];
        }else{
            result += romansMap[s[i]];
        }
    }
    return result;

};