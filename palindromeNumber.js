/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let strNum = x.toString()
    return strNum === strNum.split("").reverse().join("")
};

//O(n)