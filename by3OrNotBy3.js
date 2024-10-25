function divisibleByThree(str){
    let strArr = str.split("")
    let sum = 0
    for(let i = 0; i < strArr.length; i++){
      let num = parseInt(strArr[i])
      sum += num
    }
    return sum % 3 === 0
  }


console.log(divisibleByThree("123"))
console.log(divisibleByThree("9"))