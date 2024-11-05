/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if(needle === "" || haystack === ""){
        return 0
    }
    for(let i = 0; i < haystack.length; i++){
        if(haystack[i] === needle[0]){
            let sub = haystack.substring(i, i + needle.length);
            if(sub === needle){
                return i
            }
        }
    }
    return -1
};