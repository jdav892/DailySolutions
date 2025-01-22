export function isAllPossibilities(x: number[]): boolean {
    let numSet = new Set(x);
    let compare: number[] = []
    let newArray = Array.from(numSet)
    
    for(let i = 0; i <= x.length - 1; i++){
      compare.push(i)
    }
    compare.sort((a, b) => a - b);
    newArray.sort((a, b) => a - b);
    
    return JSON.stringify(compare) === JSON.stringify(newArray)
  }