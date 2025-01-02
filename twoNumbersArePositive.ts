export function twoArePositive(a: number, b: number, c: number): boolean {
    let match: number = 0;
    let numArr: number[] = [a, b, c]  
    for(let i = 0; i < numArr.length; i++){
      if(numArr[i] > 0){
        match += 1
      }
    }
    return match === 2;
  }