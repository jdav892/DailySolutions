function replaceChars(inputString){
    const charCount = {};
    const casedWord = word.toLowerCase()
     for (let char of casedWord){
        charCount[char] = (charChount[char] || 0) + 1;
     }

     const resultString = casedWord.split('').map(char => {
        return charCount[char] === 1 ? '(' : ')'
     }).join('');
     return resultString;
}