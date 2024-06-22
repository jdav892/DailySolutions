function remove(s, n){
    let count = 0;
    let result = '';

    for(let i = 0; i < s.length; i++){
        if(s[i] === "!" && count < n){
            count ++
        }else{
            result += s[i]
        }
    }
    return result
}