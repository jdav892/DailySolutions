function grabDoll(dolls){
    let bag = []
    for(let i = 0; i < dolls.length; i++){
        if(bag.length >= 3){
            break;
        }else if(dolls[i] !== "Hello Kitty" && dolls[i] !== "Barbie doll")
            continue;
            bag.push(dolls[i])
    }
    return bag
}