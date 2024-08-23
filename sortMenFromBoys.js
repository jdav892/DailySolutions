function menFromBoys(arr){
    let noDupes = [...new Set(arr)]
    let men = noDupes.filter(num => num % 2 === 0).sort((a, b) => a - b);
    let boys = noDupes.filter(num => num % 2 !== 0).sort((a, b) => b - a);
    
    return men.concat(boys);
  }