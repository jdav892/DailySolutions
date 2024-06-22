function towerBuilder(nfloors){
    let tower = [];
    for(let i = 0; i < nfloors; i++){
        tower.push(" ".repeat(nfloors - i - 1)
        + "*".repeat((i* 2) + 1)
        + " ".repeat(nfloors - i - 1))
    }
    return tower;
}