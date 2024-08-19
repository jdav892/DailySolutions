function adjacentElementProduct(array){
    let max = -Infinity
    for(let i = 0; i < array.length - 1; i++){
        let product = array[i] * array[i + 1]
        if(product > max){
            max = product
        }
    }
    return max
}