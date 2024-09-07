function twoHighest(arr){
    if(arr === null){
        return []
    }
    let sortedArr = [...new Set(arr)].sort((a, b) => b - a);
    if(sortedArr.length > 1){
        return [sortedArr[0], sortedArr[1]]
    }else{
        return [sortedArr[0]]
    }
}

// [...new Set(arr)].sort((a, b) => b - a).slice(0,2)