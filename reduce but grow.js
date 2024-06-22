function grow(x){
    let myArr = x
    let product = 1
    for(i = 0; i < myArr.length; i++)
    product *= myArr[i]

    return product
}



//const grow = x => x.reduce((a,b) => a*b); this was a cleaner solution to this problem that I liked