function chromosomeCheck(sperm){
    let male = /Y/i;
    if(male.match(sperm)) {
        return "Congratulations! You're going to have a son."
    }else{
        return "Congratulations! You're going to have a daughter."
    }
}

// function chromosomeCheck(sperm){
//     if(sperm === "XY"){
//         return "Congratulations! You're going to have a son."
//     }else{
//         return "Congratulations! You're going to have a daughter."
//     }
// }