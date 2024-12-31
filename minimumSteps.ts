export function minimumSteps(nums: number[], value: number) {
    let sortedArr: number[] = nums.sort((a, b) => a - b);
    let counter: number = 0;
    let compVal: number = 0;

    for(let i = 0; i < sortedArr.length - 1; i++){
        compVal += sortedArr[i]
        if(compVal >= value){
            return counter
        }
        counter ++
    }
    return counter
}