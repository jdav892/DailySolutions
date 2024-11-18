function findNb(m){
    let n = 0;
    let totalVolume = 0;
    while(totalVolume < m){
        n++
        totalVolume += Math.pow(n, 3)
    }
    
    return totalVolume === m ? n : -1
}