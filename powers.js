function numberToPower(number, power){
    let total = 1
    for(let i = 0; i < power; i++){
        total *= number
    }
    return total
}