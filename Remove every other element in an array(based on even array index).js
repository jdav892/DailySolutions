function removeEveryOther(arr){
    i = arr.length;
    while(i--)(i + 1)% 2 === 0 && arr.splice(i, 1)
    return arr
}

function removeEveryOther(arr){
    return arr.filter(function(elem, index){
        return index % 2 === 0
    });
}


const removeEveryOther = arr => arr.filter((_, i) => !(i % 2));