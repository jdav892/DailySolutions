function rentalCarCost(d){
    const dailyRate = 40;
    let totalCost = d*dailyRate;
    
    if(d >= 7) {
        totalCost -= 50;
    }else if(d >= 3){
        totalCost -= 20;
    }

    return totalCost;
}

rentalCarCost(8)



const rentalCarCost = d => d * 40 - ((d > 6) ? 50 : ((d > 2) ? 20 : 0));