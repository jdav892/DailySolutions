function array(string){
    if(string.length < 3 || string.trim() === ''){
        return null;
    }
    let splitString = string.split(',')
    if(splitString.length < 3){
        return null;
    }
    let result = splitString.slice(1, splitString.length - 1).join(" ")
    if(result.trim() === ''){
        return null;
    }
    return result;
}


//return string.split(',').slice(1, -1).join('') || null;