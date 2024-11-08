function deepCount(a){
    let count = 0;
    for(let i = 0; i < a.length; i++){
        count ++
        if(Array.isArray(a[i])){
            count += deepCount(a[i])
        }
    }
    return count
}