function declareWinner(fighter1, fighter2, firstAttacker){
    let current = first === fighter1.name ? fighter1 : fighter2;
    let opp = current === fighter1 ? fighter2 : fighter1;

        while(fighter1.health > 0 && fighter2.health > 0){
            opp.health -= current.damagePerAttack;
            let temp = current;
            current = opp;
            opp = temp;
        }
        return fighter1.health > 0 ? fighter1.name : fighter2.name
}

// function Fighter(name, health, damagePerAttack){
//     this.name = name;
//     this.health = health;
//     this.damagePerAttack = damagePerAttack;
//     this.toString = function() {return this.name;}
// } original fighter object