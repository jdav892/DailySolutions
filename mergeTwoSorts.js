function mergeArrays(arr1, arr2){
    if(!arr1 && !arr2){
        return []
    }
    let combo = arr1.concat(arr2)
    let uniqueCombo = Array.from(new Set(combo));

    return uniqueCombo.sort((a, b) => a - b);
}