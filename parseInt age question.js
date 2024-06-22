function getAge(inputString){
   let input = inputString.slice(0)
    return parseInt(input)
}

//simply returning parseInt(inputString) would work in this particular solution because the first character is an integer, and the parseInt checks the first charcter of a string and if it's not an integer it will return NaN