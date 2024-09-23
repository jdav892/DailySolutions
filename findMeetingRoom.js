function meeting(x){
    if(!x.includes('O')){
        return "None available!"
    }
    for(let i = 0; i < x.length; i++){
        if(x[i] === 'O'){
            return i
        }
    }
}