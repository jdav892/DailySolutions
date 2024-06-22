function betterThanAverage(classPoints, yourPoints){
    let sum = classPoints.reduce((acc, c) => acc + c, 0);
    let classAvg = sum / classPoints.length;
    return yourPoints > classAvg;
}