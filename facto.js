function factorial(n){
    if(n < 0 || n > 12){
        throw new RangeError
    }
    facto = 1
    for(let i = 1; i <= n; i++){
        facto *= i
    }
    return facto
}