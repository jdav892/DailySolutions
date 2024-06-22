function combat(health, damage){
    let current = health - damage;
        if(current <= 0){
            return 0;
        }else{
            return current;
        }
}