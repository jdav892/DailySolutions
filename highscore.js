function high(x){
 const xwords = x.split(' ');
 const alphaMap = {};
 for(let i = 'a'.charCodeAt(), j = 1; i <= 'z'.charCodeAt(); i++, j++){
    alphaMap[i] = j;
 }
 let highest = {word : '', score: 0};
 xwords.forEach(w => {
    const chars = w.split('');
    const sumOfChars = chars.reduce((acc, chars) => acc + alphaMap[chars.charCodeAt()], 0);
    if(sumOfChars > highest.score){
        highest = {word: w, score: sumOfChars};

    }
 });
 return highest.word
}

// in a real world problem using regex in the initial .split() would be ideal