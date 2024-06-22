function reverseLetter(str){
    let newStr = str.replace(/[^a-zA-Z]/g, '');

    return newStr.split('').reverse().join('');
}