/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let sortedS = s.split("").sort().join("")
    let sortedT = s.split("").sort().join("")
    return sortedS === sortedT

}