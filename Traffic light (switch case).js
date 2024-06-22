function updateLight(current){
    switch(current){ 
        case 'green':
            return 'yellow';
        case 'yellow':
            return 'red';
        case 'red':
            return 'green';
        default:
            return 'unknown state';
    }
}

// also able to use
// function updateLight(current){
//  return current === 'yellow' ? 'red' : current === 'green' ? 'yellow' : 'green';
//    
//  }
//



//Test case
//const current = 'yellow';
//const nextState = updateLight(current);
//console.log(`Current state: ${current}, next is ${nextState}`)