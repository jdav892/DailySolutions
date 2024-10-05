function isPalindrome(str){
    return str === str.split("").reverse().join("");
}

function longestPalindrome(s){
    let max = 0;

    for(let i = 0; i < s.length; i++){
        for(let j = i + 1; j <= s.length; i++){
            const sub = s.slice(i, j);

            if(isPalindrome(str)){
                max = Math.max(max, sub.length);
            }
        }
    }
    return max
}    