function queueTime(customers, n){
    const tills = new Array(n).fill(0)

    for(let time of customers){
        tills[0] += time
        tills.sort((a, b) => a - b);
    }
    return Math.max(...tills)
}