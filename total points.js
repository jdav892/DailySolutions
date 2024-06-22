function points(games){
    let total = 0;
    for(let i = 0; i < games.length; i++){
        const game = games[i].split(":");
        const X = parseInt(game[0]);
        const Y = parseInt(game[1]);
            if(X > Y){
                total += 3;
            }else if(X === Y){
                total += 1;
            }
    }
    return total
}