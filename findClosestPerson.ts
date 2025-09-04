function findClosest(x: number, y:number, z:number): number {
    let xDiff = Math.abs(z - x)
    let yDiff = Math.abs(z - y)

    if(xDiff < yDiff) {
        return 1
    }else if (yDiff < xDiff) {
        return 2
    }else{
        return 0
    }
}