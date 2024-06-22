function printerError(s){
    let count = 0;
    const range = 'nopqrstuvwxyz';
    for(let i = 0; i < s.length; i++){
        if(range.includes(s[i])){
            count++;
        }
    }
    return `${count}/${s.length}`;
}