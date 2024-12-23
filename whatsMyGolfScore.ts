export function golfScoreCalculator(parList: string, scoreList: string): number {
    let score: number = 0;

    let strokes: string[] = scoreList.split("")

    for(let i = 0; i < strokes.length; i++){
        score += Number(strokes[i]) - Number(parList[i])
    }
    return score 
}