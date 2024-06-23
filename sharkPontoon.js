function shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin){
    let sharkTime = sharkDistance/sharkSpeed;
    let myTime = pontoonDistance/youSpeed;
    let dolphinTime = sharkSpeed/2;

    if(sharkTime < myTime && !dolphin){
        return "Shark Bait!"
    }else if(sharkTime < myTime && dolphin){
        let sharkTime = sharkDistance/dolphinTime
    return sharkTime < myTime ? "Shark Bait!" : "Alive!"
    }else{
        return "Alive!"
    }
}


//function shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin){
//    if(dolphin){
//        sharkSpeed /= 2;
//    }
//    return ponToonDistance/youSpeed < sharkDistance/sharkSpeed ? "Alive!" : "Shark Bait!";
//}