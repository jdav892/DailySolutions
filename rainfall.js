function mean(town, strng){
    if(!town || town.trim() === "") return -1

    let towns = strng.split("\n").map(entry => entry.split(":"));
    for(let [name, data] of towns){
        if(name === town){
            let numbers = data.split(",").map(val => parseFloat(val.match(/[-+]?[0-9]*\.?[0-9]+/)));
            return numbers.reduce((sum, num) => sum + num, 0) / numbers.length;
        }
    }
    return -1
}

function variance(town, strng){
    if(!town || town.trim() === "") return -1

    let towns = strng.split("\n").map(entry => entry.split(":"));
    for(let [name, data] of towns){
        if(name === town){
            let numbers = data.split(",").map(val => parseFloat(val.match(/[-+]?[0-9]*\.?[0-9]+/)));
            let meanValue = mean(town, strng);
            let variance = numbers.reduce((sum, num) => sum + (num - meanValue)**2, 0) / numbers.length;
            return variance         
        }
    }
    return -1
}