function highestRank(arr){
    const newRank = new Map()
    arr.forEach(num => {
        if(newRank.has(num)){
            newRank.set(num, newRank.get(num) + 1)
        }else{
            newRank.set(num, 1)
        }
    });
    let max = 0;
    //Using -Infinity for smallest possible starting point for result
    let result = -Infinity;

    newRank.forEach((count, num) => {
        if(count > max || (count === max && num > result)){
            max = count;
            result = num;
        }
    })
    return result;
}