function highAndLow(numbers){
    numbers = numbers.split(" ").map(Number);
    return `${Math.max(...numbers)} ${Math.min(...numbers)}`
}