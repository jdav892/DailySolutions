function balance(left, right){
    let leftSum = 0;
    let rightSum = 0;

    for(let i = 0; i < left.length; i++){
        if(left[i] === "!"){
            leftSum += 2
        }else{
            leftSum += 3
        }
    }
    for(let j = 0; j < right.length; j++){
        if(right[j] === "!"){
            rightSum += 2
        }else{
            rightSum += 3
        }
    }

    if(leftSum > rightSum){
        return "Left"
    }else if(rightSum > leftSum){
        return "Right"
    }else{
        return "Balance"
    }

}