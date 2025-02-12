function initializeNames(name){
    let nameArr = name.split(' ')
    let newName = []

    for(let i = 0; i < nameArr.length; i++){
        if(nameArr[i] !== nameArr[0] || nameArr[i] !== nameArr[nameArr.length - 1]){
            let char = `${nameArr[i][0]}.`
            newName.push(char)
        }else{
            newName.push(nameArr[i])
        }
    }
    return newName.join(' ')
}