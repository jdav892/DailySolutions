function count(string){
    let counter = {};
    for(let char of string){
        counter[char] = (counter[char] || 0) + 1;
    }
    return counter;
}

// const count = require('lodash').countBy;