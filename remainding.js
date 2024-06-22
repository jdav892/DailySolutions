function remainder(a, b){
    let max = Math.max(a, b);
    let min = Math.min(a, b);

    if(min === 0){
        return NaN;
    }else{
        return min % max;
    }
}