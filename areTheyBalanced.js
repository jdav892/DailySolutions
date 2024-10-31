function balance(left, right){
    let leftSum = 0;
    let rightSum = 0;

    for(let i = 0; i < left.length; i++){
        left[i] === "!" ? leftSum += 2 : leftSum += 3;
    }
    for(let j = 0; j < right.length; j++){
        right[j] === "!" ? rightSum += 2 : rightSum += 3;
    }

    if(leftSum > rightSum){
        return "Left"
    }else if(rightSum > leftSum){
        return "Right"
    }else{
        return "Balance"
    }

}