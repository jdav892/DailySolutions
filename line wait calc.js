function enough(cap, on, wait){
    if(on + wait <= cap){
        return 0
    }else if(on + wait >= cap){
        return (on + wait) - cap
    }
}

//More efficient solution here may be 
//function enough(cap, wait, on){
//return (on + wait > cap) ? on + wait - cap : 0;
//
//}