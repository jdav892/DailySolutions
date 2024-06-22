function findDifference(a, b){
    let totalA = a.reduce((acc, c) => acc * c, 1);
    let totalB = b.reduce((acc, c) => acc *c, 1);

    return Math.abs(totalA - totalB)
}


// const findDifference = (a, b) => Math.abs(a.reduce((acc, c) => acc * c, 1) - b.reduce((acc, c) => acc * c, 1))