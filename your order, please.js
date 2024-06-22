function order(words){
    if(!words){
        return ""
    }
    const word = words.split(" ");
    const sorted = word.split((a , b) => {
        const numA = parseInt(a.match(/\d/)[0]);
        const numB = parseInt(b.match(/\d/)[0]);
        return numA - numB;
    });
    return sorted.join(""
    )
}