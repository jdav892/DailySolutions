function last(x){
    let splitWords = x.split(" ")
    let sortMethod = (a, b) => {
        return a[a.length - 1].charCodeAt(0) - b[b.length - 1].charCodeAt(0);
    };
    splitWords.sort(sortMethod)
    return splitWords
}

console.log(last('man i need a taxi up to ubud'))
