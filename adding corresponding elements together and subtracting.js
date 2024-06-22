var number = function(busStops){
    let sumOfFirst = busStops.reduce((acc, val) => acc + val[0], 0);
    let sumOfSecond = busStops.reduce((acc, val) => acc + val[1], 0);
    let result = sumOfFirst - sumOfSecond;
        return result;
}

// const number = (busStops) => busStops.reduce((rem, [on, off]) => rem + on - off, 0)   
//Easily the cleanest solution to this problem