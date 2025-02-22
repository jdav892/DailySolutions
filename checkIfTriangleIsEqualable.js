function equableTriangle(a, b, c){
    let s = (a + b + c) / 2
    if(a + b + c !== Math.sqrt(s * (s - a) * (s - b) * (s - c))){
        return false
    }else{
        return true
    }
}