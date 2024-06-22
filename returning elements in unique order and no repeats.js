var uniqueInOrder = function (iterable){
    if(!Array.isArray(iterable)){
        iterable = iterable.split('');
    }
    return iterable.filter((value, index, array) => {
        return value !== array[index- 1];
    });
}

//var uniqueInOrder = function(iterable){
//    return [...iterable].filter((a, i) => a !== iterable[i-1])
//}
//the cleanest written solution to this that I could find