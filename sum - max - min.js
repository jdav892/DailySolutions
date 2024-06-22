// function sumArray(array){
//     if(array.length < 2) {
//         return 0;
//     }
//     let max = Math.max(...array);
//     let min = Math.min(...array);

//     array = array.filter(num => num !== max && num !== min);

//     let sum = array.reduce((acc, curr) => acc + curr, 0);
//     return sum
// }

function sumArray(array){
    if(!Array.isArray(array) || array.length < 2){
        return 0;
    } 
    let min = Math.min(...array);
    let max = Math.max(...array);

    let sum = array.reduce((acc, curr) => acc + curr, 0);

    return sum - max - min;
}