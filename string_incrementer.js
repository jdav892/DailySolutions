function incrementString(strng){
    let newStr = strng.slice(0, -1);
    let end = strng.slice(-1).match(/[0-9]/);
    return end === null
    ? strng + "1"
    : end != 9
    ? newStr +(+end + 1)
    : incrementString(newStr) + "0";
}

//return strng.replace(/([0-8]|\d?9+)?$/, (e) => (e ? +e + 1: 1));