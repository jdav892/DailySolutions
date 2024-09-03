function datingRange(age){
    if (age <= 14){
        let min = age - .10 * age
        let max = age + .10 * age
        return `${Math.floor(min)}-${Math.floor(max)}`
    }else{
        let min = (age / 2) + 7
        let max = (age - 7) * 2
        return `${Math.floor(min)}-${Math.floor(max)}`
    }
}