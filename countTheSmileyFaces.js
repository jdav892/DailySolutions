function countSmileys(arr){
    let count = 0;
    let smileys = [':)',':D', ';)', ';D', ':-)', ';-)', ':-D', ';-D', ':~)', ';~)',':~D', ';~D']
    
    arr.forEach(smiley =>{
        if(smileys.includes(smiley)){
            count++
        }
    });
    return count
}