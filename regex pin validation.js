function validatePin(pin){
    let passW = /^(\d{4} |\d{6})$/;
    if(passW.test(pin)){
        return true;
    }else{
        return false;
    }
}