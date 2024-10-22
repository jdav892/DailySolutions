function solve(arr){
    let uniques = arr.map(subArr => [...new Set(subArr)]);
    let total = uniques.reduce((prod, sub) => prod * sub.length, 1);
    return total;
}

// const solve = arr = => arr.reduce((a ,c ) => a * new Set(c).size, 1)