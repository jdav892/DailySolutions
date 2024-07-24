function cubeOdd(arr) {
    let sum = 0;
    for(let i = 0; i < arr.length; i++){
      if(typeof arr[i] !== 'number'){
        return undefined
      }else{
        let cubed = arr[i] ** 3;
        if(cubed % 2 !== 0){
          sum += cubed
        }
      }
    }
    return sum
  }