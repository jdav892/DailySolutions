function streetFighterSelection(fighters, position, moves){
    let hovered = [];
    let currentPos = position;

    for(let move of moves){
        if(move === "up"){
            if(currentPos[0] === 0){
                hovered.push(fighters[currentPos[0]][currentPos[1]]);
            }else{
                currentPos[0]--;
                hovered.push(fighters[currentPos[0]][currentPos[1]]);
            }
        }
        if(move === "down"){
            if(currentPos[0] === 1){
                hovered.push(fighters[currentPos[0]][currentPos[1]]);
            }else{
                currentPos[0]++;
                hovered.push(fighters[currentPos[0]][currentPos[1]]);
            }
        }
        if(move === "left"){
            if(currentPos[1] === 0){
                currentPos[1] = 5
                hovered.push(fighters[currentPos[0]][currentPos[1]]);
            }else{
                currentPos[1]--;
                hovered.push(fighters[currentPos[0]][currentPos[1]]);
            }
        }
        if(move === "right"){
            if(currentPos[1] === 5){
                currentPos[1] = 0
                hovered.push(fighters[currentPos[0]][currentPos[1]]);
            }else{
                currentPos[1]++;
                hovered.push(fighters[currentPos[0]][currentPos[1]]);
            }
        }
    }
    return hovered
}