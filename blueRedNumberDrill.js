function guessBlue(blueStart, redStart, bluePulled, redPulled){
    let totalBlue = blueStart - bluePulled;
    let totalRed = redStart - redPulled;
    let totalVal = totalBlue + totalRed;
    return totalBlue/totalVal
}