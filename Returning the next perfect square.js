function findNextSquare(sq){
    const power = Math.sqrt(sq)
    if(Number.isInteger(power)){
        const square = Math.pow(power + 1, 2);
            return square;
        }else{
        }
        return -1;
}

//function findNextSquare(sq){
//    return Math.sqrt(sq)%1 -1 : Math.pow(Math.sqrt(sq)+1,2)
//}
