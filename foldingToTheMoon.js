function foldTo(distance){
    let foldThickness = 0.0001
    let total = 0
    if(distance < 0){
        return null
    }
    if(distance === 0){
        return 0
    }
    while(foldThickness < distance){
        foldThickness *= 2
        total ++
    }
    return total
}