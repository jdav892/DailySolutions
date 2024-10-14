// Create a function called args_count that returns the number of arguments provided
function args_count(){
    let count = 0
    for(let i = 0; i < arguments.length; i++){
        if(arguments){
            count++
        }
    }return count
}

