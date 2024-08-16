function sortArray(array){
    const oddSort = array.filter(num => num % 2 !== 0).sort((a ,b) => a - b);

    return array.map(num =>(num % 2 !== 0 ? oddSort.shift() : num));
}
// due to so many array copies I believe this is a rather slow solution and more expensive in terms of memory than the use of a couple loops that add to an array