reverse = function(array){
    let revArr = []
    for(let i = 0; i < array.length; i++){
        revArr.unshift(array[i])
    }
    return revArr
}