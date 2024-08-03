function tidyNumber(n){
    let strN = n.toString();
    let sortedArr = [...strN].sort((a, b) => a - b);
    return strN === sortedArr.join('');
}