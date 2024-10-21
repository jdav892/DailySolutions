function partList(arr){
    let result = [];

    for(let i = 1; i < arr.length; i++){
        let one = arr.slice(0, i);
        let two = arr.slice(i);
        result.push([one.join(" "), two.join(" ")]);
    }
    return result;
}