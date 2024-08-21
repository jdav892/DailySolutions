function pointsPer48(ppg, mpg){
    if(ppg === 0 || mpg === 0){
        return 0
    }
    let actualPpg = (ppg/mpg) * 48
    return Math.round(actualPpg * 10) / 10
}

