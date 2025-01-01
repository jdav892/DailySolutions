export function getScore(arr: number[]) {
    let bonus: number[] = [0, 40, 100, 300, 1200];
    let score: number = 0;
    let levelCount: number = 0;
    let current: number = 0;

    for(let i = 0; i < arr.length; i++){
        if(arr[i] > 0){
            score += bonus[arr[i]] * (levelCount + 1);
        }
        current += arr[i]
        if(current >= 10){
            levelCount += Math.floor(current / 10);
            current %= 10;
        }
    }
    return score;
}