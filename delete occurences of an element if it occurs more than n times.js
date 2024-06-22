function deleteNth(arr, n){
    let count = {}
    let result = arr.filter((i) => {
        count[i] = (count[i] || 0) + 1;
        return count[i] <= n
    });
    return result
}


// function delenteNth(arr, n){
//    let count = {};
//    return arr.filter(function(i) {
//        count[i] = (count[i] || 0) + 1;
//        return count[i] <= n;
//    });
//}