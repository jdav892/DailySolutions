function sum(numbers){
    let numArr = [...numbers];
    let sum = numArr.reduce((acc, curr) => acc + curr, 0);{
        return sum
    }
}

// const sum = numbers => numbers.reduce((acc, curr) => acc + curr, 0)