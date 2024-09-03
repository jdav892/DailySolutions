function firstToLast(str, c){
    let first = str.indexOf(c);
    let last = str.indexOf(c);

    if(first === -1){
        return -1
    }
    return last - first;
}