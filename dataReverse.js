function dataReverse(data) {
    let converter = [];
    let start = 0;
    let end = 8;
    let section = data.slice(start, end);
    let loopLength = data.length/8;
    converter.unshift(section.join(""))
    
    for(let i = 1; i < loopLength; i++){
       start += 8;
       end += 8;
       section = data.slice(start, end)
       converter.unshift(section.join(""));
    }
    let swap = converter.join("");
    let newConv = swap.split("");
    let newStore = [];
    for(let i = 0; i < data.length; i ++){
      newStore.push(parseInt(newConv[i]))
    }
    return newStore
    
  }