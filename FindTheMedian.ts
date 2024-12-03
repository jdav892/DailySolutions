export function median(n: number[]):number {
    const sortedArr: number[] = n.sort((a, b) => a - b);
    const len: number = sortedArr.length;
    if (sortedArr.length % 2 === 0){
        const med1: number = sortedArr[len / 2 - 1];
        const med2: number = sortedArr[len / 2];
        return (med1 + med2) / 2; 
    }
    return sortedArr[Math.floor(len / 2)];
  }