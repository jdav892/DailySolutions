function catMouse(x){
    let catAndMouse = [...x];
    return Math.abs(catAndMouse.indexOf('C') - catAndMouse.indexOf('m')) > 4 ? "Escaped!" : "Caught!"
}