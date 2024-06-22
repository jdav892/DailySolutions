function bump(x){
    let nCount = 0;
    for(let i = 0; i < x.length; i++){
        if(x[i] === "n"){
            nCount++
        }
    }if(nCount > 15){
        return "Car Dead"
    }else{
        return "Woohoo!"
    }
}

// const bump => (x) => x.split('n').length > 16 ? "Car Dead" : "Woohoo!"