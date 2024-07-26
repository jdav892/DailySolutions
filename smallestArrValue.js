function min(arr, toReturn){
    let minValue = Math.min(...arr)
        if(toReturn === "value"){
            return minValue
        }else if(toReturn === "index"){
            return arr.indexOf(minValue)
        }
}