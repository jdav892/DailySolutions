function countSheeps(sheep){
    if(sheep === null || sheep === undefined){
        return 0;
    }
    let count = 0;
    for(let i = 0; i < sheep.length; i++)
    if(sheep[i] === true){
        count++;
    }

    return count
}



// function countSheeps(arrayOfSheeps){
//     return arrayOfSheeps.filter(Boolean).length;
// }