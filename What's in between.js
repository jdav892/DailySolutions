function between(a, b){
    if (a > b){
    //checks if a > b and if it is, they swap them
        [a, b] = [b, a];
    }
    //array.from with a range of numbers
    return Array.from({length: b - a + 1}, (_, index) => a + index);
}

//chatgpt algoritmn response, could be refactored well however I don't know how I'd approach this yet.