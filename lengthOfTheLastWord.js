var lengthOfLastWord = function(s) {
    let newStr = s.trim();
    let index = newStr.length;
    let length = 0;
    while(newStr[index] == " "){
        index -= 1;
    }

    while(index >= 0 && newStr[index] != " "){
        length += 1;
        index -=1;
    }
    return length - 1;

}