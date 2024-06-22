function longest(s1,s2){
    let longer = s1 + s2;
    let unique = new Set(longer);
    let sortedArray = Array.from(unique).sort();
    let sortedString = sortedArray.join('');
    return sortedString
}