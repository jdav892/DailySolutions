const findAll = (array, n) => {
    let store = [];
    for(let i = 0; i < array.length; i++){
        if(array[i] === n){
            store.push(i)
        }
    }
    return store;
}