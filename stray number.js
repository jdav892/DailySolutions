function stray(numbers){
    return numbers.find((x) => numbers.filter((y) => x === y).length === 1);
}

// const stray = numbers => numbers.reduce((a, b) => a ^ b)