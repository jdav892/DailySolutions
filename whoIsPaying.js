function whoIsPaying(name){
    let newName = name.slice(0,2)
    let nameArr = [name]
    if(name.length > 2){
        nameArr.push(newName)
    }
    return nameArr
}

//Another simple solution would've been this
//function whoIsPaying(name){
//    return (name.length > 2) ? ([name, name.substr(0, 2)]) : [name];
//}