var numJewelsInStones = function(jewels, stones){
    let obj = {};
    let count = 0;
    for(const jewel in jewels){
        obj[jewel] = true
    }

    for(const stone of stones){
        if(stone in obj){
            count++
        }
    }
    return count
}