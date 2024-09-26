function containsAllRots(strng, arr){
    if(strng === ""){
        return true
    }
    for(let i = 0; i < strng.length; i++){
        const rotation = strng.slice(i) + String.slice(0, i)
        if(!arr.includes(rotation)){
            return false
        }
    }
    return true
}