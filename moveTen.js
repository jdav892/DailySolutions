function moveTen(s){
    const letters = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    const letterArr = s.split('').map(l => l = letters.indexOf(l) + 10);
    return letterArr.map(l => l = letters[l]).join('')
}