function elevatorDistance(array){
    let count = 0;
    for(let i = 0; i < array.length - 1; i++){
        if(array.length < 3 && arr[0] == arr[1]){
            return 0
        }else if(array[i] !== array[-1]){
            let diff = Math.abs(array[i + 1] - array[i]);
            count += diff
        }else{
            count -= array[i]
        }
    }
    return count
}