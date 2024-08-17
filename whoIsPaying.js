function whoIsPaying(name){
    let newName = name.slice(0,2)
    let nameArr = [name]
    if(name.length > 2){
        nameArr.push(newName)
    }
    return nameArr
}