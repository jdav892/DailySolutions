function newAvg(arr, newavg){
    const current = arr.reduce((sum, donation) => sum + donation, 0);
    const total = newavg * (arr.length + 1)
    const next = total - current

    if(next <= 0){
        throw new Error("Expected New Average is too low")
    }
    return Math.ceil(next)
}