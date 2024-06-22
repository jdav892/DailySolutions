function multiply(number){
    let exps = Math.abs(number).toString().length;
    return number * (5 ** exps)
}