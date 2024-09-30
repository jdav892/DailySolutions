function nbDig(n, d){
    let count = 0;
    for(let i = 0; i <= n; i++){
        const square = (i * i).toString();
        for(const char of square){
            if(char == d){
                count++
            }
        }
    }
    return count
}

//function nbDig(n, d){
//    let num = '';
//    for(let i = 0; i <= n; i++){
//        num += Math.pow(i, 2);
//    }
//    return num.split(d).length - 1
//}