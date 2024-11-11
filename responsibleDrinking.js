function hydrate(s){
    let count = 0;
    for(let i = 0; i < s.length; i++){
        const num = parseInt(s[i])
        if(!Number.isNaN){
            count += num
        }
    }
    return count > 1 ? `${count} glasses of water` : '1 glass of water';
} 
