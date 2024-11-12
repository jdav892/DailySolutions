function solution(pairs){
    let newArr = [];
    for(const[key, value] of Object.entries(pairs)){
        let kvp = `${key} = ${value}`;
        newArr.push(kvp);
    }
    return newArr.join(",");
}